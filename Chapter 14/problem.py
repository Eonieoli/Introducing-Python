# 1
import os

print(os.listdir('.'))


# 2
print(os.listdir('..'))


# 3
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'wt') as f:
    f.write(test1)


# 4
with open('test.txt', 'rt') as f:
    test2 = f.read()

print(test1)
print(test2)
print(test1 == test2)