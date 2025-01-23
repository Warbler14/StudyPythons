import sys

print(sys.version)

paths = sys.path
for path in paths:
    print(path)

a = 10234
print(sys.getrefcount(a))

