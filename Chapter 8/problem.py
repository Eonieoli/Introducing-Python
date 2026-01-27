# 1
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f)

# 2
print(e2f['walrus'])

# 3
f2e = {}
for key, value in e2f.items():
    f2e[value] = key
print(f2e)

# 4
print(f2e['chien'])

# 5
print(list(e2f.keys()))

# 6
life = {
    "animals": {"cats": "Henri", "octopi": "Grumpy", "emus": "Lucy"},
    "plants": {},
    "other": {}
}
print(life)

# 7
print(list(life.keys()))

# 8
print(list(life['animals'].keys()))

# 9
print(life['animals']['cats'])

# 10
squares = {number: number ** 2 for number in range(10)}
print(squares)

# 11
odd_set = {number for number in range(10) if number % 2 == 1}
print(odd_set)

# 12
# 제너레이터 배우고 다시

# 13
attitudes = ('optimist', 'pessimist', 'troll')
thoughts = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

# think = {}
# for attitude, thought in zip(attitudes, thoughts):
#     think[attitude] = thought

think = {attitude: thought for attitude, thought in zip(attitudes, thoughts)}
print(think)

# 14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']

movies = {title: plot for title, plot in zip(titles, plots)}
print(movies)