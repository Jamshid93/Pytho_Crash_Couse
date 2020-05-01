# bu yerda 1 dan 1000000 gacha bo'lgan sonlarni eng katta va enga kichigini topish va bu sonlarni yigíndisini hisoblash
# 1 dan 1000000gacha sonlarni yigíndisini topish for loopdan foydalanib
digits=[]
for value in range(1,1000001):
    digits.append(value)
print("min=",min(digits))
print("max=",max(digits))
print("sum=",sum(digits))