# bu yerda bir vaqtni o'zida bir qancha shartlarni tekshirishni ko'ramiz, and , or  kabi kalit so'zlar yordamida.
age_0=18
age_1=22 
age_0=22
print(age_0 >= 21 and age_1 >= 21 ) # agar and foydalansak bu berilgan shart ikkala tomonini xam qoniqtirishi kerak degani bo'ladi.

# Endi shu yerda or kalit so'zidan foydalanamiz bu degani 
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) # bu agar or dan foydalalnsak tengsizlikning kamida bittasi hsartni qanoalantirsa bo'ldi degani
# unda bizga True qaytaradi.

 # Agar biz age_0 ni xam o'zgartiradigan bo'lsak Fulse qaytaradi
age_0 = 17
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
