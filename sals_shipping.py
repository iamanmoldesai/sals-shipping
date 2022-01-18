#!/usr/bin/env python
# coding: utf-8

# In[1]:


weight = 41.5

#Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20.00
else:
  cost = weight * 4.75 + 20.00

#Final Print
if weight <= 1:
  print("Cost of Ground Shipping for package weighing " + str(weight) + " pound is $" + str(cost))
else:
  print("Cost of Ground Shipping for package weighing " + str(weight) + " pounds is $" + str(cost)) 


#Ground Shipping Premium Charges

cost_of_premium_ground_shipping = 125
print("Cost of Ground Shipping Premium is Flat $" + str(cost_of_premium_ground_shipping))

#Drone Shipping

if weight <= 2:
  cost = weight * 4.50 
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25

#Final Print
if weight <= 1:
  print("Cost of Drone Shipping for package weighing " + str(weight) + " pound is $" + str(cost))
else:
  print("Cost of Drone Shipping for package weighing " + str(weight) + " pounds is $" + str(cost)) 


# In[ ]:




