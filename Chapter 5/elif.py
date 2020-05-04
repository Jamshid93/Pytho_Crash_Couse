# bu yerda if ni ichidagi blokda elifdan qanday foydalansihni ko'ramiz
# bu degani o'zi agar if deb biron bir shratni e'lon qilganimizdan so'ng yana qandaydir shartni elon qilmoqchi bo'lsak kerak bo'ladi
# deylik bizga parkka kirmoqchi bo'lganga narxlar insonning yoshiga nisbattan taqsimlangan bo'lsin
# masalan , 4 yoshgacha bo'lganlarga tekin, 4-18 yosh bo'lganlarga 25$, 18 yoshdan kattalarga 40 $ qilib belgilangan bo'lsa
# buni quydagicha test qilamiz
age = int(input("Your age: "))
if age < 4:
    price = 0
elif age < 18: 
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")  # bu yerda men formating stringdan foydalandim. 