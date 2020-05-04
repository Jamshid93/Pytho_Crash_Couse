# bu yerda xam if shart operatori xaqida gaplashamiz 
# deylik bizga saylovlarda ovor berish jarayonida u ovoz beruvchining 18 yoshga kirgan yoki kirmaganini tekshirish kerak bo'lsa
age = int(input("Please write your age:"))
if age >= 18:
    print("You are old enough to vote!") # biz if shart opertoridan foydalaganimizda xoxlaganimizcha printdan foydalansak bo'ladi malasan 
# deylik bizga yana shundan keyin "Siz registratsiya ya'ni roýxatdan o'tganmisiz degan so'rovni bersin"
    print("Have you registered to vote yet?")
else:   # bu els degani agar bu yuqoridagi shartni qanoatlantirmasa bunday qil degani.
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
