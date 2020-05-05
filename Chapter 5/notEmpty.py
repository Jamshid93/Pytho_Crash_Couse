# endi e'lon qilingan listda elemeti bormi yuqmi shuni for loop ishga tushishidan olsin aniqlash kerak bo'lsa
requested_toppings = [ ]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")