
def get_binary(number, fill):
    result = []
    while number > 0:
        rm = int(number % 2)
        rst = str(rm)
        result.insert(0, rst)
        number = int(number / 2)
    return ''.join(result).zfill(fill)


for num in range(0, 16):
    print(get_binary(num, 4))

print(get_binary(1234, 4*3))