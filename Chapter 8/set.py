# empty_set = set()
# print(empty_set)
# even_numbers = {0, 2, 4, 6, 8}
# print(even_numbers)
# odd_numbers = {1, 3, 5, 7, 9}
# print(odd_numbers)

# print(set('letters'))

# print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))


# reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
# print(len(reindeer))


# s = set((1, 2, 3))
# print(s)
# s.add(4)
# print(s)


# s = set((1, 2, 3))
# s.remove(3)
# print(s)


# furniture = set(('sofa', 'ottoman', 'table'))
# for piece in furniture:
#     print(piece)


# drinks = {
#     'martini': {'vodka', 'vermouth'},
#     'black russian': {'vodka', 'kahlua'},
#     'white russian': {'cream', 'kahlua', 'vodka'},
#     'manhattan': {'rye', 'vermouth', 'bitters'},
#     'screwdriver': {'orange juice', 'vodka'}
# }

# for name, contents in drinks.items():
#     if 'vodka' in contents:
#         print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#         print(name)


# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
#         print(name)

# bruss = drinks['black russian']
# wruss = drinks['white russian']

# a = {1, 2}
# b = {2, 3}

# print(a & b)
# print(a.intersection(b))
# print(b & a)
# print(b.intersection(a))

# print(bruss & wruss)
# print(wruss & bruss)

# print(a | b)
# print(a.union(b))
# print(b | a)
# print(b.union(a))

# print(bruss | wruss)
# print(wruss | bruss)

# print(a - b)
# print(a.difference(b))
# print(b - a)
# print(b.difference(a))

# print(bruss - wruss)
# print(wruss - bruss)

# print(a ^ b)
# print(a.symmetric_difference(b))
# print(b ^ a)
# print(b.symmetric_difference(a))

# print(bruss ^ wruss)
# print(wruss ^ bruss)

# print(a <= b)
# print(a.issubset(b))
# print(b <= a)
# print(b.issubset(a))

# print(bruss <= wruss)
# print(wruss <= bruss)

# print(a < b)
# print(b < a)

# print(bruss < wruss)
# print(wruss < bruss)

# print(a >= b)
# print(a.issuperset(b))
# print(b >= a)
# print(b.issuperset(a))

# print(bruss >= wruss)
# print(wruss >= bruss)

# print(a >= a)
# print(a.issuperset(a))
# print(a <= a)
# print(a.issubset(a))

# print(a > b)
# print(b < a)

# print(wruss > bruss)
# print(bruss > wruss)

# print(a > a)


# a_set = {number for number in range(1, 6) if number % 3 == 1}
# print(a_set)


# print(frozenset([3, 2, 1]))
# print(frozenset(set([2, 1, 3])))
# print(frozenset({1, 2, 3}))
# print(frozenset((2, 3, 1)))

# fs = frozenset([3, 2, 1])
# print(fs)
# # fs.add(4)


# marx_list = ['Groucho', 'Chico', 'Harpo']
# marx_tuple = ('Groucho', 'Chico', 'Harpo')
# marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
# marx_set = {'Groucho', 'Chico', 'Harpo'}
# print(marx_list[2])
# print(marx_tuple[2])
# print(marx_dict['Harpo'])
# print('Harpo' in marx_list)
# print('Harpo' in marx_tuple)
# print('Harpo' in marx_dict)
# print('Harpo' in marx_set)


# marxes = ['Groucho', 'Chico', 'Harpo']
# pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
# stooges = ['Moe', 'Curly', 'Larry']

# tuple_of_lists = marxes, pythons, stooges
# print(tuple_of_lists)

# list_of_lists = [marxes, pythons, stooges]
# print(list_of_lists)

# dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
# print(dict_of_lists)

# houses = {
#     (44.79, -93.14, 285): 'My House', (38.89, -77.03, 13): 'The White House'
# }