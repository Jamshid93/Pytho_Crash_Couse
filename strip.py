# bu yerda shu whitespace ya'ni stringa qo'shilgan bo'sh joylarni probellarni qanday qilib olib tashlashni ko'rib chiqamiz
favroite_lenguage="Python  "
print(favroite_lenguage.rstrip()) # bu rstrip() degan method ya'ni shu r degani right - o'ng degani o'ng tomondan qo'shilgan 
# probelni olib tasglaydi
favroite_lenguage="  C++" 
print(favroite_lenguage.lstrip()) # bu lstrip() degan method ya'ni left-chap degani chap tomondan olib tashla qo'shilgan
# probelni degani 
favroite_lenguage="  Python   "
print(favroite_lenguage.strip()) # bu strip() degani method ya'ni ikkita tomondan xam qo'shilgan probellari olib tashlaydi