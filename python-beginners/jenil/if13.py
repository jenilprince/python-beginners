units = int(input("Electricity unit: "))
if units <= 50:
    charge = units*.5
    add = 20/100* charge
    tot = charge + add
    print(f"Charge: {tot}")
if units > 50 and units <= 150:
    charge = 50*.5 + (units - 50)*.75
    add = 20/100* charge
    tot = charge + add
    print(f"Charge: {tot}")
elif units > 150 and units <= 250:
    charge = 50*.5 + 100*.75 + (units - 150)*1.2
    add = 20/100* charge
    tot = charge + add
    print(f"Charge: {tot}")
elif units > 250:
    charge = 50*.5 + 100*.75 + 100*1.2 + (units - 250)*1.5
    add = 20/100* charge
    tot = charge + add
    print(f"Charge: {tot}")
