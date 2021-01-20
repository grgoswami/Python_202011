#Menu 
foods = [ 
    { "item":"Pasta",        "price":3.00 },
    { "item":"Pizza",        "price":3.00 },
    { "item":"Garlic knot",  "price":1.00 },
    { "item":"Burger",       "price":4.00 },
    { "item":"French Fries", "price":1.00 },
    { "item":"Hot dog",      "price":1.50 },
    { "item":"rice",         "price":1.00 }
]
"""
drinks = [
    { "item":"Water",    "price":0.50 },
    { "item":"Coke",     "price":1.00 },
    { "item":"Lemonade", "price":1.50 },
    { "item":"orange_juice, "price":1.50 }
]

sweets = [
    { "item":"Ice cream", "price":2.50 },
    { "item":"Candy",     "price":0.50 },
    { "item":"Cupcake",   "price":1.50 },
    { "item":"S'more",    "price":1.00 }
]
"""
name = input("Hello, what is your name? ")
print("Hi " + name + ", here is the food menu:")
for i in range(len(foods)):  
    print(str(i) + " -- " + foods[i]["item"] + ", " + str(foods[i]["price"]))

print("If you are done, just enter '-1 -1'")


total_money = 0
while(True):
    # asking order
    item_idx, quantity = input("what would you like to order for foods (item, quantity)? ").split()
    
    # if no orders, break the while loop
    if int(item_idx) < 0: 
        break
    elif int(item_idx) >= len(foods):
        print("Bad input, food index must between 0 and " + str(len(foods)-1))
        continue
    
    # print what's ordered
    print("You ordered " + str(quantity) + " " + foods[int(item_idx)]["item"] + ("s" if int(quantity)>1 else ""))
    
    # how much are these items
    money = foods[int(item_idx)]["price"] * int(quantity)
    total_money = total_money + money
    
print("You need to pay a total of $" + str(total_money) + " for foods")





