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


# import re

# source = 'Young Frankenstein'
# m = re.split('n', source)
# print(m)


# import re

# source = 'Young Frankenstein'
# m = re.sub('n', '?', source)
# print(m)


# import string
# import re

# printable = string.printable
# print(len(printable))
# print(printable[0:50])
# print(printable[50:])

# print(re.findall('\d', printable))
# print(re.findall('\w', printable))
# print(re.findall('\s', printable))

# x = 'abc' + '-/*' + '\u00ea' + '\u0115'
# print(re.findall('\w', x))

# import re

# source = '''I wish I may, I wish I might
# Have a dish of fish tonight.'''

# print(re.findall('wish', source))
# print(re.findall('wish|fish', source))
# print(re.findall('^wish', source))
# print(re.findall('^I wish', source))
# print(re.findall('fish$', source))
# print(re.findall('fish tonight.$', source))
# print(re.findall('fish tonight\.$', source))
# print(re.findall('[wf]ish', source))
# print(re.findall('[wsh]+', source))
# print(re.findall('ght\W', source))
# print(re.findall('I (?=wish)', source))
# print(re.findall('(?<=I) wish', source))
# print(re.findall('\bfish', source))
# print(re.findall(r'\bfish', source))


import re

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))