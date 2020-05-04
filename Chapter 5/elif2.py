# bu yerda elif dan qanday ikki marta va bundan xam ko'p foydalansihni ko'ramiz
# umuman olganda qancha biz tekshiradigan xolatlar ko'p bo'lsa shuncha marta elifdan foydalanib ketaversak bo'ladi
#deylik bizga parkka kirmoqchi bo'lganga narxlar insonning yoshiga nisbattan taqsimlangan bo'lsin
# masalan , 4 yoshgacha bo'lganlarga tekin, 4-18 yosh bo'lganlarga 25$, 18 yoshdan kattalarga 40 $ qilib belgilangan bo'lsa}
# va agar 65 yoshdan katta odamlar uchun chegirma qilib bilet narxini 20 $ qilib belgilqmoqchi bo'lsak 
# uydagicha bo'ladi
age = int(input("Your age: "))
if age < 4:
    price = 0
elif age < 18: 
    price = 25
elif age < 65:
    price = 40
elif age >=65:
    price = 20
# biz xar doim xam if blokni oxirida elsedan foydalanishimiz shart emas agar xoxlasak uni tushurib xam qoldirib elif bilan yakunlasak xam bo'ladi
#else:
#    price = 20

print(f"Your admission cost is ${price}.")