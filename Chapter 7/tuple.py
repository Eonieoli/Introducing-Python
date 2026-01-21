# empty_tuple = ()
# print(empty_tuple)

# one_marx = 'Groucho',
# print(one_marx)

# one_marx = ('Groucho',)
# print(one_marx)

# one_marx = ('Groucho')
# print(one_marx)

# marx_tuple = 'Groucho', 'Chico', 'Harpo'
# print(marx_tuple)

# one_marx = 'Groucho',
# print(type(one_marx))
# print(type('Grouch',))
# print(type(('Groucho',)))

# marx_tuple = ('Groucho', 'Chico', 'Harpo')
# a, b, c = marx_tuple
# print(a)
# print(b)
# print(c)

# password = 'swordfish'
# icecream = 'tuttifrutti'
# password, icecream = icecream, password
# print(password)
# print(icecream)

# marx_list = ['Groucho', 'Chico', 'Harpo']
# print(tuple(marx_list))

# print(('Groucho',) + ('Chico', 'Harpo'))

# print(('yada',) * 3)

# a = (7, 2)
# b = (7, 2, 9)
# print(a == b)
# print(a <= b)
# print(a < b)

# words = ('fresh', 'out', 'of', 'ideas')
# for word in words:
#     print(word)

# t1 = ('Fee', 'Fie', 'Foe')
# t2 = ('Flop',)
# t1 += t2
# print(t1)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))