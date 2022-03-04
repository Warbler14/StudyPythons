# -*- coding: utf-8 -*-

import textwrap

message = "Life is too short, you need python."
print(textwrap.shorten(message, width=15))
print(textwrap.shorten(message, width=15, placeholder='...'))

long_text = (message + ' ') * 5
message_len = len(message)
print(message_len)
result = textwrap.wrap(long_text, width=message_len)
print(result)
for string in result:
    print(string)

print('-----')
print('\n'.join(result))

print('-----')
long_text = message * 5
result = textwrap.fill(long_text, width=70)
print(result)