# empty_dict = {}
# print(empty_dict)

# bierce = {
#     "day": "A period of twenty-four hours, mostly misspent",
#     "positive": "Mistaken at the top of one's voice",
#     "misfortune": "The kind of fortune that never misses",
# }
# print(bierce)


# acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
# print(acme_customer)

# acme_customer = dict(first="wile", middle="E", last="Coyote")
# print(acme_customer)

# x = dict(name="Elmer", def="hunter")


# lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(lol))

# lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
# print(dict(lot))

# tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
# print(dict(tol))

# los = ['ab', 'cd', 'ef']
# print(dict(los))

# tos = ('ab', 'cd', 'ef')
# print(dict(tos))


# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
# }
# print(pythons)

# pythons['Gilliam'] = 'Gerry'
# print(pythons)

# pythons['Gilliam'] = 'Terry'
# print(pythons)

# some_pythons = {
#     'Graham': 'Chapman',
#     'John': 'Cleese',
#     'Eric': 'Idle',
#     'Terry': 'Gilliam',
#     'Michael': 'Palin',
#     'Terry': 'Jones',
# }
# print(some_pythons)


# print(some_pythons['John'])

# # print(some_pythons['Groucho'])

# print('Groucho' in some_pythons)

# print(some_pythons.get('John'))

# print(some_pythons.get('Groucho', 'Not a Python'))

# print(some_pythons.get('Groucho'))


# signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
# print(signals.keys())

# print(list(signals.values()))

# print(list(signals.items()))


# print(len(signals))


# first = {'a': 'agony', 'b': 'bliss'}
# second = {'b': 'bagels', 'c': 'candy'}
# print({**first, **second})

# third = {'d': 'donuts'}
# print({**first, **third, **second})


# pythons = {
#     'Chapman': 'Graham',
#     'Cleese': 'John',
#     'Gilliam': 'Terry',
#     'Idle': 'Eric',
#     'Jones': 'Terry',
#     'Palin': 'Michael',
# }
# print(pythons)

# others = {'Marx': 'Groucho', 'Howard': 'Moe'}

# pythons.update(others)
# print(pythons)

# first = {'a': 1, 'b': 2}
# second = {'b': 'platypus'}
# first.update(second)
# print(first)


# del pythons['Marx']
# print(pythons)
# del pythons['Howard']
# print(pythons)


# print(len(pythons))
# print(pythons.pop('Palin'))
# print(len(pythons))
# # pythons.pop('Palin')


# print(pythons.pop('First', 'Hugo'))
# print(len(pythons))


# pythons.clear()
# print(pythons)
# pythons = {}
# print(pythons)


# pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
# print('Chapman' in pythons)
# print('Palin' in pythons)

# print('Gilliam' in pythons)


# signals = {
#     'green': 'go',
#     'yellow': 'go faster'
#     'red' 'smile for the camera'
# }
# save_signals = signals
# signals['blue'] = 'confuse everyone'
# print(save_signals)


# signals = {
#     'green': 'go',
#     'yellow': 'go faster',
#     'red': 'smile for the camera'
# }
# original_signals = signals.copy()
# signals['blue'] = 'confuse everyone'
# print(signals)
# print(original_signals)


# signals = {
#     'green': 'go',
#     'yellow': 'go faster',
#     'red': ['stop', 'smile']
# }
# signals_copy = signals.copy()
# print(signals)
# print(signals_copy)

# signals['red'][1] = 'sweat'
# print(signals)
# print(signals_copy)

# import copy
# signals = {
#     'green': 'go',
#     'yellow': 'go faster',
#     'red': ['stop', 'smile']
# }
# signals_copy = copy.deepcopy(signals)
# print(signals)
# print(signals_copy)
# signals['red'][1] = 'sweat'
# print(signals)
# print(signals_copy)


# a = {1:1, 2:2, 3:3}
# b = {3:3, 1:1, 2:2}
# print(a == b)

# a = {1:1, 2:2, 3:3}
# b = {3:3, 1:1, 2:2}
# print(a <= b)

# a = {1: [1, 2], 2: [1], 3: [1]}
# b = {1: [1, 1], 2: [1], 3: [1]}
# print(a == b)


# accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
# for card in accusation: # or, for card in accusation.keys()
#     print(card)

# for value in accusation.values():
#     print(value)

# for item in accusation.items():
#     print(item)

# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)


# word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in word}
# print(letter_counts)

# word = 'letters'
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# print(letter_counts)

# vowels = 'aeiou'
# word = 'onomatopoeia'
# vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
# print(vowel_counts)