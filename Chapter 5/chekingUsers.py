# deyik bizga saytdan faol foydalanayotganlarni aniqlash yoki yangi foydalanuvchilar xaqida aniqlash shularni 
# alohida listlar bilan ishlatish kerak bo'lsa
current_users=["lola","bobur","lee","jamshid","jhon","marry"]
new_users=["david","kristina","jamshid","alex","lee"]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is available")
    else:
        print(f"{new_user} will need to enter a new username")

