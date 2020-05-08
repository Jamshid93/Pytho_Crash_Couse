# dictionary dan foydalanganimizda unda berilgan kalit so'zlar orqali uni qiymatini yangi boshqa bir o'zgaruvchiga ta'minlashimiz
# mumkin yoki aynana shu biz so'ragan kalit so'zning qiymatini chiqarib beradi
alien_0 = {'color': 'green'}
print(alien_0['color']) # xozir shu yerda bizga 'green' degan rangni chiqarib beradi

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points'] # bu yerda esa yangi o'zgaruvchiga ta'minlayapmiz va shu kalis so'z orqali uni qiymatini chiqaramiz
print(f"You just earned {new_points} points!")