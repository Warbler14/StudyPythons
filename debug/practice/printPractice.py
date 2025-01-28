import math

# while
print('-------------------------------------------------------------------')
limit = 19
length = math.floor(math.sqrt(limit))
count = 1
while count < limit:
    if count < length:
        print(f" {count}", end="")
    elif count % length != 0:
        if count + 1 == limit:
            print(f" {count}")
        else:
            print(f" {count}", end="")
    else:
        print(f" {count}")
    count += 1


print('-------------------------------------------------------------------')
a = 0
r = 0
while a < 100:
    a += 1
    if a % 2 == 0:
        continue

    if r < 9:
        if a < 10:
            print(f"  {a}", end="")
        else:
            print(f" {a}", end="")
        r = r + 1

    elif r >= 9:
        print(f" {a}")
        r = 0

print('-------------------------------------------------------------------')

a = 0
r = 0
while a < 100:
    a = a + 1
    if a % 2 == 1:
        continue

    if r < 9:
        if a < 10:
            print(f"  {a}", end="")
        else:
            print(f" {a}", end="")
        r = r + 1

    elif r >= 9:
        print(f" {a}")
        r = 0
print('-------------------------------------------------------------------')

x = 0
y = 0

while x < 5:
    x = x + 1
    y = 0
    while y < (x-1):
        print('*', end=''),
        y = y + 1
    print('*')

print('-------------------------------------------------------------------')
x = 0
y = 5

while x < 5:
    x = x + 1
    y = 0
    while y < (5-x):
        print('*', end=''),
        y = y + 1
    print('*')

print('-------------------------------------------------------------------')

x = 0
y = 0

while x < 5:
    x = x + 1
    y = 0
    while y < 4:
        if y < (x-1):
            print(' ', end=''),
        else:
            print('*', end=''),
        y = y + 1
    print('*')

print('-------------------------------------------------------------------')

x = 0
y = 0

while x < 5:
    x = x + 1
    y = 0
    while y < 4:
        if y < (5-x):
            print(' ', end=''),
        else:
            print('*', end=''),
        y = y + 1
    print('*')

print('')
print('-------------------------------------------------------------------')

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
full_name = "{}.{}".format(first_name, last_name)
message = f"Hello, {full_name.title()}!"
print(message)