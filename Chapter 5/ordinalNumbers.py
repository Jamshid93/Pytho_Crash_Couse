# deylik bizga 1 dan 9 gacha raqamlar iborat list e'lon qilingan bo'lsin
# biz shu raqamlarni tartib sonni ko'rsatadigan qilib chop etishimiz kerak
# masaln Birinchi(1st),ikkinchi(2nd).....
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    elif number==4:
        print("4th")
    elif number==5:
        print("5th")
    elif number==6:
        print("6th")
    elif number==7:
        print("7th")
    elif number==8:
        print("8th")
    else:
        print("9th")

# yoki shuni boshqacha xam qilib yozsa bo'ladi
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")