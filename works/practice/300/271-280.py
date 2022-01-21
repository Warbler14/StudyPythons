# -*- coding: utf-8 -*-
import random

print("-=-271-=-")
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3


acc = Account("김이박", 100)
print(acc.name)
print(acc.balance)
print(acc.bank)
print(acc.account_number)

print("-=-272-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1

kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)

print("-=-273-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)


kim = Account("김민수", 100)
lee = Account("이민수", 100)
park = Account("박이김", 100)
Account.get_account_num()


print("-=-274-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

park = Account("박이김", 100)
park.deposit(10)
print(park.balance)


print("-=-275-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            return amount
        else:
            print("canceled")


park = Account("박이김", 100)
park.withdraw(10)
print(park.balance)
park.withdraw(100)
print(park.balance)

print("-=-276-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return amount
        else:
            print("canceled")

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ','), "원")


p = Account("파이썬", 10000)
p.display_info()


print("-=-277-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        self.deposit_count = 0
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01
            self.deposit_count += 1


    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return amount
        else:
            print("canceled")

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ','), "원")


p = Account("파이썬", 10000)
p.display_info()
for i in range(5):
    p.deposit(10)
p.display_info()


print("-=-278-=-")
accounts = []
accounts.append(Account("파이썬", 10000000))
accounts.append(Account("김이박", 1000000))
accounts.append(Account("이박김", 100000))
accounts.append(Account("박김이", 10000))
for account in accounts:
    account.display_info()


print("-=-279-=-")
for account in accounts:
    balance = account.balance
    if balance >= 1000000:
        account.display_info()

print("-=-280-=-")
class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "MyBank"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + '-' + num2 + '-' + num3
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        Account.account_count += 1


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(str(amount))
            self.balance += amount
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01
            self.deposit_count += 1


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(str(amount))
            self.balance -= amount
            return amount
        else:
            print("canceled")

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.account_number)
        print("잔고:", format(self.balance, ','), "원")

    def deposit_history(self):
        for history in self.deposit_log:
            print(history)

    def withdraw_history(self):
        for history in self.withdraw_log:
            print(history)


p = Account("파이썬", 10000)
p.display_info()
for i in range(5):
    p.deposit(10)
p.deposit_history()

for i in range(5):
    p.withdraw(10)
p.display_info()
p.withdraw_history()
