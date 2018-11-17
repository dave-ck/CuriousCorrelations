import json
import os
patients = {}

def findConditions(jsonDict):
    conditions = []
    for i in jsonDict:
        i=1

"""Resource types:
Organization
Patient
Encounter
Claim
Observation
Procedure
Immunization
Encounter
Claim
MedicationRequest
"""







def addPatient(filename):
    jsonFile = open(filename, "r")
    jsonString = jsonFile.read()
    dict = json.loads(jsonString)
    for i in dict["entry"]:
        mySet.add(i["resource"]["resourceType"])
        print("Resource type: ", i["resource"]["resourceType"])
        """for j in i["resource"]:
            print(j)"""
    print(mySet)



#addPatient("fhir/Abbott701_Victor476_24.json")
# print(dict["entry"]["resource"]["status"]
mySet = {1}
for i in os.listdir("fhir"):    #for every patient in the dataset
    jsonFile = open("fhir/"+i, "r")
    jsonString = jsonFile.read()
    dict = json.loads(jsonString)
    for i in dict["entry"]:
        mySet.add(i["resource"]["resourceType"])

print(mySet)