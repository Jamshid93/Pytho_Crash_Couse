# bu yerda not in dkalit so'zlaridan foydalanaishni ko'ramiz: bu kalist so'zlar xam bizda listni tekshirishimizda kerak bo'ladi
# masalan bizga biron bir wep saytda yoki chatda bir foydalanuvchining komment yozishi mumkinmi yoki yo'qmi shuni qarab chiqamiz
# deylik bir qancha faydalanuvchilar turli sabablarga ko'ra banned qilingan ya'ni komment yozsih u foydalanuvchilar uchun yopilgan
# yangi boyagi komment yozmoqchi bo'lgan foydalanuchining shu taqiqlanganlar orasida bormi yuqligini tekshirish so'ralgan bo'lsa
# biz uni not in kalit so'zi yordamida amalga oshiramiz
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users: # bu degani agar shu user da ko'rsatilgan foydalanuchi yuqoridagi banned qilingan roýxatda bo'lmasa unga ruxsat ber degani
    print(f"{user.title()}, you can post a response if you wish.")