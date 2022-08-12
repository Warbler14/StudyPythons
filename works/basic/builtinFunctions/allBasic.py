# -*- coding: utf-8 -*-

boolean_list = ['True', 'True', 'True']

# The all() function returns True if all elements in the given iterable are true
# if not, it returns False
result = all(boolean_list)
print(result)   # True

# all value true
boolean_list = [1, 3, 5, 7, 9]
print(all(boolean_list))    # True

# all values false
boolean_list = [0, False]
print(all(boolean_list))    # False

# one false value
boolean_list = [1, 3, 5, 7, 0]
print(all(boolean_list))    # False

# one true value
boolean_list = [False, 0, 100]
print(all(boolean_list))    # False

# empty iterable
boolean_list = []
print(all(boolean_list))    # True

string_value = "test"
print(all(string_value))    # True

string_value = "0"
print(all(string_value))    # True

string_value = ""
print(all(string_value))    # True

dict_value = {0: 'False', 1: 'False'}
print(all(dict_value))      # False

dict_value = {1: 'False', 2: 'False'}
print(all(dict_value))      # True

dict_value = {2: 'True', 3: 'True'}
print(all(dict_value))      # True

dict_value = {4: 'True', 5: 'False'}
print(all(dict_value))      # True

dict_value = {1: 'True', False: 'False'}
print(all(dict_value))      # False

dict_value = {1: 'True', False: '0'}
print(all(dict_value))      # False

dict_value = {1: 'True', False: ''}
print(all(dict_value))      # False

dict_value = {}
print(all(dict_value))      # True

dict_value = {'0': 'True'}
print(all(dict_value))      # True

dict_value = {0: 'True'}
print(all(dict_value))      # False
