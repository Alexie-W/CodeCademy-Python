weight = 4.8
cost_premium = 125.00
drone_weight = 4.8

#Ground Shopping
if weight <= 2: 
  cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost = weight * 4 + 20
else: 
  cost = weight * 4.75 + 20

print(cost)
print(cost_premium)

#Drone Shipping
if drone_weight <= 2:
  drone_cost = drone_weight * 4.5
elif drone_weight > 2 and drone_weight <=6:
  drone_cost = drone_weight * 9
elif drone_weight > 6 and drone_weight <= 10: 
  drone_cost = drone_weight * 12
else: 
  drone_cost = drone_weight * 14.25

print(drone_cost)
