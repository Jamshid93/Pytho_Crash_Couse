# deylik bizga bitta listni e'lon qilamiz ismlardan iborat list lekin ichida 'admin' degani xam bo'ladi
# agar shu adminga to'g'ri kelsa boshqa narsa deb, qolgan  ismlarga to'g'ri kelsa boshqa narsa deb chiqarish kerak bo'lsa
usernames=["admin","Jhon","Marry","Jamshid","Bobur","Lola"]
for username in usernames:
    if username=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")