#store the items in dictonary

menu={
    'pizza':80,
    'burgur':60,
    'salad':50,
    'coffee':40
}

capitalized_menu = {}

# Looping through the menu items
for item in menu:
   item.capitalize()

print("Welcome to our restorent what do you like to order")
print("*****Menu*****\n1.pizza:80rs\n2.burgur:60rs\n3.salad=50rs\n4.coffee:40rs\n")

order_total=0

item1=input("Enter the item you want:")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your item {item1} has been added")
else:
    print(f"ordered item {item1}is not available in the menu")

another_item=input("Do you want to order another item (yes/no):")
if (another_item=="yes"):
    item2=input("Enter the name of 2nd item:")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"item {item2} has been added")
    else:
        print(f"ordered item {item2}is not available in the menu")

print(f"the total amount is {order_total}")


