import json
data_to_add={"Name": "Jenil",
             "Age": 18,
             "key": "value",
             "key2": "value2",
             "key3": "value3"}
with open("j.json","w") as file:
    json.dump(data_to_add,file)
with open("j.json","r") as file:
    data=json.load(file)
    print(data["Name"])
