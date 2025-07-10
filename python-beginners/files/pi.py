import  pickle
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("new.pkl", "wb") as f:
    pickle.dump(data, f)
with open("new.pkl", "rb") as f:
    d=pickle.load(f)
    print(d)