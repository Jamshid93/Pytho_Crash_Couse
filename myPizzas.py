# bu yerda xam slicing bilan ishlaymiz listda 
# bizga bitta pizza degan list berilgan shunga yangi pizza qo'shamiz, undan copy olamiz, va xar bir copy qilingan 
# listga yangi pizza qo'shamiz boshqa boshqa qilingan
pizzas=["meat pizza", "cheez pizza","fruit pizza"]
your_pizzas=pizzas[:]
pizzas.append("chocolote pizza")

your_pizzas.append("cold pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My fiend's favorite pizzas are:")
for pizza in your_pizzas:
    print(pizza)
    