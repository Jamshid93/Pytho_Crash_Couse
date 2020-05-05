# bu yerda endi elifni ishlatib bo'lmaydigan xolatlarni ko'ramiz
# deylik bizga bitta pizza larni nomidan iborat list berilgan desak, umuman biron bir odam pizzani buyurtma bermoqchi bo'lsa
# unda elifni ishlatib bo'maydi sababi unda agar elifni ishlatsak faqat birinchisini chiqarib beraveradi
# shu uchun unday xolatlarda faqat if dan foydalanamiz
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")