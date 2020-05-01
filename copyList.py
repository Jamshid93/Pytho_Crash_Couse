# Endi bu yerda listni qanday qilib copy qilishni ko'ramiz
my_foods=["Plov","Pizza","Lag'man","Tuxum sho'rva"]
friend_foods=my_foods[:] # bu degani xuddi elon qilgan listdagini koçhirib kompiya qilib ol degani

# Endi agar bizga men yotirgan boshqa ovqatni qo'shish , do'stim yoqtirgan boshqa ovqatni qo'shish kerak bo'lsa.
my_foods.append("Coca cola")
friend_foods.append("Ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Agar biz [:] belgidan foydalanmsak ikkita listni shunchaki tenglashtirib qoýsak unda nima qo'shsak xam ikkala listda 
# bir xilda chiqaveradi natija ya;ni ikkoviga xam bir xilda qo'shaveradi.
friend_foods=my_foods 

my_foods.append("Coca cola")
friend_foods.append("Ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)