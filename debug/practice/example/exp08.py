# if elif else
# ----------------------------------------------
score = 90

if score > 100:
    print('score > 100')
elif score > 50:
    print('score > 50')
else:
    print('score > 0')

# ----------------------------------------------
a = 10
if a > 5:
    print('Big')
else:
    print('Small')

# ----------------------------------------------
order = 'spagetti'
price = 0
if order == 'spam':
    price = 500
elif order == 'ham':
    price = 700
elif order == 'egg':
    price = 300
elif order == 'spagetti':
    price = 900

print(price)
# ----------------------------------------------
order = 'egg'
menu = {'spam': 500, 'ham': 700, 'egg': 300, 'spagetti': 900}
price = menu[order]
print(price)

# ----------------------------------------------
score = int(input('score : '))

if score >= 95:
    print('degree A++')
elif score >= 90:
    print('degree A')
elif score >= 85:
    print('degree B++')
elif score >= 80:
    print('degree B')
elif score >= 75:
    print('degree C++')
elif score >= 70:
    print('degree C')
elif score >= 65:
    print('degree D++')
elif score >= 60:
    print('degree D')
else:
    print('degree F')
# ----------------------------------------------
