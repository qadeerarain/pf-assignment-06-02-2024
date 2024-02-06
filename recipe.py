3. Recipe Calculator: Design a recipe calculator that adjusts ingredient quantities based on the 
number of servings. Use variables to store recipe ingredients and amounts, and write 
expressions to calculate adjusted quantities.

servings=int(input("enter the number of servings"))

wheat_per_servings=100
rice_per_servings=60

total_wheat=wheat_per_servings*servings
total_rice=rice_per_servings*servings


print(f"for {servings} servings, you'15 need: ")

print(f"{total_wheat} grams of wheat")
print(f"{total_rice} grams of rice")


