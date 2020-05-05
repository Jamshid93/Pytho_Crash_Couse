alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

# bu xuddi shu misolni boshqqacha ko'rinishi
alien_color = 'red'
if alien_color=='green':
    earned=5
elif alien_color=='yellow':
    earned=10
elif alien_color=='red':
    earned=15
print(f"You just earned {earned} points!")