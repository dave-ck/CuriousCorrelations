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
    patientAttributes.update({"AllergyIntoleranceNumber": len(patientDict["AllergyIntolerances"])})
    patientAttributes.update({"ImmunizationNumber": len(patientDict["Immunizations"])})
    patients.append(patientAttributes)

    for i in patientDict["Observations"]:
        print(i)

addPatient("fhir/Abshire734_Alfred968_16.json")

def populate():
    for i in os.listdir("fhir")[:900]:  # for the first 100 patients in the dataset
        addPatient("fhir/" + i)


def getDataCollection(varx, vary):
    collection = []
    for i in patients:
        collection.append((i[varx], i[vary]))
    return collection

def getMetaData(varx, vary):
    return None


#TODO - read birthdate in as date not String

discreteValues = ["gender", "multipleBirthBoolean", "maritalStatus", "languageCode", "country"]
continuousValues = ["birthYear", "AllergyIntoleranceNumber", "ImmunizationNumber"]

for i in patients:
    print(i["birthYear"])