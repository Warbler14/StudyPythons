import re

data = \
"""Geon 010-1111-2222
Ha 010-3333-4444"""

pattern = re.compile("(\d{3})[-](\d{4})[-](\d{4})")
print(pattern.sub("\g<1>-****-\g<3>", data))
