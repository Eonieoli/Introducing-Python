# import re

# result = re.match('You', 'Young Frankenstein')
# print(result)

# youpattern = re.compile('You')
# result = youpattern.match('Young Frankenstein')
# print(result)


# import re

# source = 'Young Frankenstein'
# m = re.match('You', source)

# if m:
#     print(m.group())

# m = re.match('^You', source)

# if m:
#     print(m.group())

# import re

# source = 'Young Frankenstein'
# m = re.match('Frank', source)

# if m:
#     print(m.group())

# import re

# source = 'Young Frankenstein'

# if m := re.match('Frank', source):
#     print(m.group())

# import re

# source = 'Young Frankenstein'
# m = re.search('Frank', source)

# if m:
#     print(m.group())

# import re

# source = 'Young Frankenstein'
# m = re.match('.*Frank', source)

# if m:
#     print(m.group())


# import re

# source = 'Young Frankenstein'
# m = re.search('Frank', source)

# if m:
#     print(m.group())


# import re

# source = 'Young Frankenstein'
# m = re.findall('n', source)
# print(m)
# print('Found', len(m), 'matches')

# import re

# source = 'Young Frankenstein'
# m = re.findall('n.', source)
# print(m)

# import re

# source = 'Young Frankenstein'
# m = re.findall('n.?', source)
# print(m)


import re

source = 'Young Frankenstein'
m = re.split('n', source)
print(m)