# bu yerda pop() methodi xaqida bu method xam listni oxirgi elementini olib faqat shu elemetni bizga chiqarib beradi
car=["BMW","Ford","WolcsWagen","Nexia"]
car1=car.pop() # pop() methodidan foydalanish shunday amalga oshiriladi
print(car) # Agar biz pop() dan keyin birinchi listni o'zini print qiladigan bo'lsak oxirgi list elemetini olib tashlaydi
print(car1)
car2=car.pop(0) # bu yerda index bilan ishlash shu 0 indexdagini olib tashla degani
print(car)
print(car2)