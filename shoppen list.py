2. Shopping List: Write a program to manage a shopping list. Use variables to store item names, 
quantities, and prices. Calculate the total cost of items and check if you have enough budget.



s={"mango":100,"apple":60,"vegetables":150,"guava":80}

#taking user input for budget
b=int(input("enter the number of budget: "))
print("available items and their prices:")
print(s)

#user input for items name and quantity
n=int(input("enter the items name you want to buy"))
q=int(input("enter the quantity  you want to buy "))
      
#calculating the total cost of the select item and quantity
def total_cost(item,quantity,prices):
    return prices.get(item,0)*quantity
    
t=total_cost(n,q,s)
#check the if the total cost within budget
def check_budget(total_cost,budget):
    if total_cost<=budget:
        return "within budget"
    else:
        return "out of budget"
x=check_budget(t,b)

#printing the result
print(f"total cost for {n} {q} (s) is {t}")
print(f"budget for: {x}")

