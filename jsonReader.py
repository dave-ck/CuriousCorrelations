import json
import os

patients = {}

resourceTypes = {'CarePlan', 'Organization', 'Condition', 'MedicationRequest', 'Procedure', 'Encounter', 'Goal',
                 'Patient',
                 'Observation', 'DiagnosticReport', 'Immunization', 'Claim', 'AllergyIntolerance'}

# load resources from all patients where resourceType = x
patientDict = {"PatientInfo": None, "Procedures": [], "Immunizations": [], "Conditions": [],
               "DiagnosticReports": [], "AllergyIntolerances": []}

# below: writing the patientDict for one patient
jsonFile = open("fhir/Abbott701_Victor476_24.json", "r")
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
    elif not i["resource"]["resourceType"] in {'CarePlan', 'Organization', 'Encounter', 'Goal',
                                               'Observation', 'Claim', 'MedicationRequest'}:
        print("Problem! Resource type", i["resource"]["resourceType"], "not caught in if statement!")

# at this stage, a *slightly* more usable dict has been generated - resources split by type

# below : assign attributes from each resource type to the patient
patientAttributes = {}
for i in ['gender', 'birthDate', 'multipleBirthBoolean']:
    patientAttributes.update({i: patientDict["PatientInfo"][i]})
# calculate age


# marital status
patientAttributes.update({'maritalStatus': patientDict["PatientInfo"]["maritalStatus"]["text"]})
# language
patientAttributes.update({"languageCode": patientDict["PatientInfo"]["communication"][0]["language"]["coding"][0]["code"]})
# may be bodge, uses index 0 which max not be the case with other pts
for i in ['extension', 'address', 'communication']:
    print(i, ":", patientDict["PatientInfo"][i])

print(patientAttributes)


def addPatient(filename):
    jsonFile = open(filename, "r")
    jsonString = jsonFile.read()
    dict = json.loads(jsonString)
    for i in dict["entry"]:
        resourceTypes.add(i["resource"]["resourceType"])
        print("Resource type: ", i["resource"]["resourceType"])
        """for j in i["resource"]:
            print(j)"""
    print(resourceTypes)


# addPatient("fhir/Abbott701_Victor476_24.json")
# print(dict["entry"]["resource"]["status"]


"""

for i in patientDict:
   print(i, ": ", len(patientDict[i]), "entries")


resourceTypes = {1}
for i in os.listdir("fhir"):  # for every patient in the dataset
    jsonFile = open("fhir/" + i, "r")
    jsonString = jsonFile.read()
    dict = json.loads(jsonString)
    for i in dict["entry"]:
        resourceTypes.add(i["resource"]["resourceType"])
resourceTypes.remove(1)
print(resourceTypes)"""
