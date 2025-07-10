'''person={"name": "Alice",
        "age": 30,
        "city": "New York"}
print(person["age"])
print(person.get("age"))
car={"make": "Tesla",
     "model": "Model X"}
car["year"] = 2021
print(car)
pers1={"name": "Alice",
       "age": 30,
       "city": "New York"}
pers1["age"] = 32
print(pers1)
pers2={"name": "Alice",
       "age": 30,
       "city": "New York"}
del pers2["city"]
print(pers2)
pers3={"name": "Alice",
       "age": 30,
       "city": "New York"}
popped = pers3.pop("age")
print(pers3)
print(popped)
pers5={"name": "Alice",
       "age": 30,
       "city": "New York"}
pers5.clear()
print(pers5)
pers6={"name": "Alice",
       "age": 30,
       "city": "New York"}
for key in pers6.items():
    print(key)
for value in pers6.values():
    print(value)
for key, value in pers6.items():
    print(key, ':', value)'''
a="alen"
print(a.find("a"))