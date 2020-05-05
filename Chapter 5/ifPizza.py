# deylik bizga pizza tayyorlashdan nimalar yani qanday mxasulotlarni qo'shib tayyorlash kerak bo'lsa
# litda bu maxsulatlar berilgan bo'lsa uni birinchi for orqali chiqarib ko'ramiz
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# To'g'ri bu xolatda xammasi bexato ishladyi xamma maxsultni qo'shgan xolda pizza tayyor bo'ladi
# Lekin agar shu yerda ya'ni listda ko'rsatilgan biron bir maxsulot tugab qolgan bo'lsa nima bo'lishini
# bu xolatni qanday xal qilishni ko'ramiz
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")