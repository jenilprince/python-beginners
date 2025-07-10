import  pandas as pd
new=pd.read_csv("new.csv")
po=new.sort_values(by="Name",ascending=True)
print(po)
print(new)