import numpy as np
price=np.array([100,200,300])
quantity=np.array([1,2,3])
total_cost=price*quantity
print(f"Total cost = {total_cost}")
discount=total_cost*25/100
print(f"Discount = {discount}")