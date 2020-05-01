# deylik bizga 1 dan 10 gacha bo'lgan sonlarni kubini chiqarish so'ralgan bo'lsin....
# masaln 2**3=8
numbers=list(value**3 for value in range(1,11))
print(numbers)

# yoki buni 
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)