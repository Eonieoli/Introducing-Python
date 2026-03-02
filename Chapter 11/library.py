# periodic_table = {'Hydrogen': 1, 'Helium': 2}
# print(periodic_table)

# carbon = periodic_table.setdefault('Carbon', 12)
# print(carbon)

# helium = periodic_table.setdefault('Helium', 947)
# print(helium)
# print(periodic_table)


# from collections import defaultdict
# periodic_table = defaultdict(int)

# periodic_table['Hyrogen'] = 1
# print(periodic_table['Lead'])
# print(periodic_table)


# from collections import defaultdict

# def no_idea():
#     return 'Huh?'

# bestiary = defaultdict(no_idea)
# bestiary['A'] = 'Abominable Snowman'
# bestiary['B'] = 'Basilisk'
# print(bestiary['A'])
# print(bestiary['B'])
# print(bestiary['C'])

# bestiary = defaultdict(lambda: 'Huh?')
# print(bestiary['E'])


# from collections import defaultdict

# food_counter = defaultdict(int)
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     food_counter[food] += 1

# for food, count in food_counter.items():
#     print(food, count)


# dict_counter = {}

# for food in ['spam', 'spam', 'eggs', 'spam']:
#     if food not in dict_counter:
#         dict_counter[food] = 0
#     dict_counter[food] += 1

# for food, count in dict_counter.items():
#     print(food, count)


# from collections import Counter

# breakfast = ['spam', 'spam', 'eggs', 'spam']
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)

# print(breakfast_counter.most_common())
# print(breakfast_counter.most_common(1))

# print(breakfast_counter)
# lunch = ['eggs', 'eggs', 'bacon']
# lunch_counter = Counter(lunch)
# print(lunch_counter)

# print(breakfast_counter + lunch_counter)
# print(breakfast_counter - lunch_counter)
# print(lunch_counter - breakfast_counter)

# print(breakfast_counter & lunch_counter)
# print(breakfast_counter | lunch_counter)


# quotes = {
#     'Moe': 'A wise guy, huh?',
#     'Larry': 'Ow!',
#     'Curly': 'Nyuk nyuk!',
# }

# for stooge in quotes:
#     print(stooge)


# from collections import OrderedDict
# quotes = OrderedDict([
#     ('Moe', 'A wise guy, huh?'),
#     ('Larry', 'Ow!'),
#     ('Curly', 'Nyuk nyuk!'),
# ])

# for stooge in quotes:
#     print(stooge)


# def palindrome(word):
#     from collections import deque
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#     return True

# print(palindrome('a'))
# print(palindrome('racecar'))
# print(palindrome(''))
# print(palindrome('radar'))
# print(palindrome('halibut'))


# def another_palindrome(word):
#     return word == word[::-1]

# print(another_palindrome('radar'))
# print(another_palindrome('halibut'))


# import itertools

# for item in itertools.chain([1, 2], ['a', 'b']):
#     print(item)


# import itertools

# for item in itertools.cycle([1, 2]):
#     print(item)


# import itertools

# for item in itertools.accumulate([1, 2, 3, 4]):
#     print(item)


# import itertools

# def multiply(a, b):
#     return a * b

# for item in itertools.accumulate([1, 2, 3, 4], multiply):
#     print(item)


# from pprint import pprint
# from collections import OrderedDict

# quotes = OrderedDict([
#     ('Moe', 'A wise guy, huh?'),
#     ('Larry', 'Ow!'),
#     ('Curly', 'Nyuk nyuk!'),
# ])

# print(quotes)
# pprint(quotes)


