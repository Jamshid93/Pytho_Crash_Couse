# bu yerda if shart operatorini ko'rib chiqamiz
# deylik bizga bir qancha mashinalarni nomlaridan iborat list berilgan bo'lsa, shu yerdan bitta moshinani katta xarflar bilan
# qolgan moshinalarning faqat bosh xarfini katta xarflar bilan chiqarish kerak bo'lsa , if operatoridan foydalgan xolda
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
     if car == 'bmw':
        print(car.upper())
     else:
        print(car.title())