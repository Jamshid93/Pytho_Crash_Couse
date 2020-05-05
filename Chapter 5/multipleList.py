# deylik mizoj xoxlagan maxsulot turi ya'ni pizzaga qo'shadigan maxsulot biz e'lon qilgan listda yuq bo'lsa
# ya'ni shu pizza tayyorlaydigan joyda unda qanday bo'ladi
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!") 