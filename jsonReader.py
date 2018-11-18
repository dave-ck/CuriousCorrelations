import json
import os

patients = []

resourceTypes = {'CarePlan', 'Organization', 'Condition', 'MedicationRequest', 'Procedure', 'Encounter', 'Goal',
                 'Patient',
                 'Observation', 'DiagnosticReport', 'Immunization', 'Claim', 'AllergyIntolerance'}

def addPatient(filename):
    patientDict = {"PatientInfo": None, "Procedures": [], "Immunizations": [], "Conditions": [],
                   "DiagnosticReports": [], "AllergyIntolerances": [], "Observations":[]}
    jsonFile = open(filename, "r")
    jsonString = jsonFile.read()
    dict = json.loads(jsonString)
    for i in dict["entry"]:
        if i["resource"]["resourceType"] == "Patient":
            patientDict["PatientInfo"] = i["resource"]
        elif i["resource"]["resourceType"] == "Procedure":
            patientDict["Procedures"].append(i)
        elif i["resource"]["resourceType"] == "Immunization":
            patientDict["Immunizations"].append(i)
        elif i["resource"]["resourceType"] == "Condition":
            patientDict["Conditions"].append(i)
        elif i["resource"]["resourceType"] == "DiagnosticReport":
            patientDict["DiagnosticReports"].append(i)
        elif i["resource"]["resourceType"] == "AllergyIntolerance":
            patientDict["AllergyIntolerances"].append(i)
        elif i["resource"]["resourceType"] == "Observation":
            patientDict["Observations"].append(i)
        elif not i["resource"]["resourceType"] in {'CarePlan', 'Organization', 'Encounter', 'Goal',
                                                   'Claim', 'MedicationRequest'}:
            print("Problem! Resource type", i["resource"]["resourceType"], "not caught in if statement!")

    # at this stage, a *slightly* more usable dict has been generated - resources split by type

    # below : assign attributes from each resource type to the patient
    patientAttributes = {}
    for i in ['gender', 'multipleBirthBoolean']:
        if i in patientDict["PatientInfo"]:
            patientAttributes.update({i: patientDict["PatientInfo"][i]})

    patientAttributes.update(({'birthYear':int(patientDict["PatientInfo"]["birthDate"][:4])}))

    # marital status
    patientAttributes.update({'maritalStatus': patientDict["PatientInfo"]["maritalStatus"]["text"]})
    # language
    patientAttributes.update({"languageCode": patientDict["PatientInfo"]["communication"][0]["language"]["coding"][0][
        "code"]})  # may be bodge, uses index 0 which max not be the case with other pts
    for i in patientDict["PatientInfo"]["address"]:
        if "country" in i:
            patientAttributes.update({"country": i["country"]})
        # TODO extract latitude, longitude
        """
        for j in i:
            if "extension" in j:
                for k in j["extension"]:
                    print(k)
                    if "extension" in k:
                        print(k)
                    print(j["valueDecimal"])
                    patientAttributes.update({"latitude":j["valueDecimal"]})
        """
    weight = 0
    height = 0
    bmi = 0
    for i in patientDict["Observations"]:
        if "text" in i["resource"]["code"]:
            if i["resource"]["code"]["text"] == "Body Weight":
                weight = max(weight, i["resource"]["valueQuantity"]["value"])
            elif i["resource"]["code"]["text"] == "Body Height":
                height = max(height, i["resource"]["valueQuantity"]["value"])
            elif i["resource"]["code"]["text"] == "Body Mass Index":
                bmi = max(bmi, i["resource"]["valueQuantity"]["value"])
    if weight != 0:
        patientAttributes.update({"weight" : weight})
    if height != 0:
        patientAttributes.update({"height" : height})
    if bmi != 0:
        patientAttributes.update({"bmi" : bmi})
    patientAttributes.update({"AllergyIntoleranceNumber": len(patientDict["AllergyIntolerances"])})
    patientAttributes.update({"ImmunizationNumber": len(patientDict["Immunizations"])})

    patients.append(patientAttributes)


def populate():
    for i in os.listdir("fhir")[:900]:  # for the first 100 patients in the dataset
        addPatient("fhir/" + i)


def getDataCollection(varx, vary):
    collection = []
    for i in patients:
        if varx in i and vary in i:
            collection.append((i[varx], i[vary]))
    return collection

def getMetaData(varx, vary):
    return None

populate()

print(getDataCollection("weight", "height"))
#TODO - read birthdate in as date not String

discreteValues = ["gender", "multipleBirthBoolean", "maritalStatus", "languageCode", "country"]
continuousValues = ["birthYear", "AllergyIntoleranceNumber", "ImmunizationNumber", "weight", "height", "bmi"]
