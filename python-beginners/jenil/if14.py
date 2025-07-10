basic = int(input("Basic Salary: "))
if basic <= 10000:
    hra = .2* basic
    da = .8*basic
    total = basic+da+hra
    print(f"Gross salary = {total}")
elif basic >= 10001 and basic <= 20000:
    hra = .25*basic
    da = .9*basic
    total = basic+da+hra
    print(f"Gross salary = {total}")
elif basic >= 20001:
    hra = .3*basic
    da = .95*basic
    total = basic+da+hra
    print(f"Gross salary = {total}")

