def add(a, b):
    return a + b


addlambda = lambda a, b: a+b


def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result


def print_key_word_args(**args):
    print(args)


def add_and_mul(a, b):
    return a + b, a * b


# 초기화시키고 싶은 매개변수는 항상 뒤쪽에
def print_self(name, age, sex='man'):
    print('name is %s' % name)
    print('age %d years old' % age)
    print('%s' % sex)


print(add(20, 10))
print(addlambda(1, 3))
print(add([1, 2, 3], [1, 2, 3]))
print(add(b=[4, 5, 6], a=[1, 2, 3]))
print(add_many(1, 3, 5, 7, 9, 11, 13))
print('add : ', add_mul('add', 1, 3, 5, 7, 9, 11, 13))
print('mul : ', add_mul('mul', 1, 3, 5, 7, 9, 11, 13))
print_key_word_args(name='test', age=20)
print(add_and_mul(20, 10))
result1, result2 = add_and_mul(3, 5)
print(result1, result2)
print_self('tom', 21)
print_self('katherine', 19, 'woman')
