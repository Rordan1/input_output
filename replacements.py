print("what would you like to eat\n")
menu = ["chicken", 10, "steak", 25, "pork", 15]

print(menu)

choice = input()

if choice == "chicken":
    print(menu[1])

elif choice == "steak":
    print(menu[3])

if choice == "pork":
    print(menu[5])


menu_2 = menu + ["fish", 20]



#elif choice == "":
   # print("unfortunately this item is not available, please refer to our specials menu for new daily items") + print(menu_2)

print('"you have selected "choice"') + print("we also have a specials menu")

print(menu_2[6])

choice_2 = input()

if choice_2 == menu_2[6]:
    print(menu_2[7])