import json
data={"name":"alen",
      "age":18,
      "location":"piravom"}
with open("j.json","w") as file:
    json.dump(data,file)
with open("j.json","r") as file:
    a=json.load(file)
    print(a["name"])
    print(a["location"])



