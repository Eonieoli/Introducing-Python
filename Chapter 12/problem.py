# 1
import unicodedata

mystery = '\U0001f4a9'
print(unicodedata.name(mystery))


# 2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)


# 3
print(pop_bytes.decode())


# 4
f = open('mammoth.txt', 'r')
mammoth = f.read()
print(mammoth)
f.close()


# 5
import re

c_result = re.findall(r"\bc\w*\b", mammoth)
print(c_result)


# 6
c4_result = re.findall(r"\bc\w{3}\b", mammoth)
print(c4_result)


# 7
r_result = re.findall(r"\b\w*r\b", mammoth)
print(r_result)


# 8
aeiou_result = re.findall(r"\b\w*[aeiou]{3}\w*\b", mammoth)
print(aeiou_result)


# 9


# 10


# 11