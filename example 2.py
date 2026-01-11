#A shop gives a discount of 10% if the total bill is more than 1000.
# Write a Python program that: Stores the prices of three items in variables and calculates the total using arithmetic operators.
# Uses a relational operator to check if the total is greater than 1000.
# Prints whether the customer is eligible for a discount or not.

item1 = 450
item2 = 450
item3 = 100
totalbill = item1 + item2 + item3
if totalbill>1000:
    print("The customer is eligible for 10% discount") 
else:
    print("The customer is not eligible for discount")