# bu yerda f-string xaqida bu degani ikkita sting turidagi o'zgaruvchini bitta qilib qo'shib chiqarish bir qatorga degani
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}" # mana shu f-string ya'ni formatting string deyiladi.
print(full_name)
 
# bundan tashqari buni boshqacha ko'rinishlarda xam qo'llash mumkin.
print(f"Hello, {full_name.title()}!")

# yoki boshqa bitta o'zgaruvchiga ta'minlagan xolda
massage=f"Hello, {full_name.title()}!"
print(massage)
