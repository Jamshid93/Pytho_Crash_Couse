# bu yerda range() function yordamida bir qancha amallarni ko'ramiz masalan bizga 1 dan 10 gacha bo'lgan
# sonlarning kvadratlarini chiqarish kerak bo'lsa
squares=[]
for value in range(1,11): # bu degani agar bizga 10 soni xam kerak bo'lsa 11 gacha deb kirtish kerak .
    squuare=value**2
    squares.append(squuare)

print(squares)

# Endi xuddi shu kodni qisqaroq xam yozish mumkin bu yuqoridagi tushunarliroq qilib yozsih uchun edi
squares=[]
for value in range(1,11): 
    squares.append(value**2)
print(squares)

# bu yerda List Comprehensions degan narsaga to'xtalamiz bu degani e'lon qilgan listimizni ichida turli xil ammalardan foydalanishimiz
# mumkin degani deylik bizga 1 dan 10 gacha sonlarni kvadratini chiqarish kerak bo'lsin
squares=[value**2 for value in range(1,11)]
print(squares)