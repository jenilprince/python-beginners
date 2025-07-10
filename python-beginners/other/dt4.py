from datetime import date, timedelta
d=date.today()
new=date(d.year+1,1,1)
newyear=new-d
print(newyear)