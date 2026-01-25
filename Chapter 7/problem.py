# 1
years_list = [1995, 1996, 1997, 1998, 1999]

# 2
print(years_list[3])

# 3
print(years_list[-1])

# 4
things = ['mozzarella', 'cinderella', 'salmonella']

# 5
print(things[1].capitalize())

# 6
print(things[0].upper())

# 7
things.remove('salmonella')
print(things)

# 8
surprise = ['Groucho', 'Chico', 'Harpo']

# 9
print(surprise[-1].lower()[::-1].capitalize())

# 10
even_numbers = [number for number in range(10) if number % 2 == 0]
print(even_numbers)

# 11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone bette"

for i in range(len(rhymes)):
    for j in range(len(start1)):
        print(f"{start1[j].capitalize()}!", end=' ')
    print(f"{rhymes[i][0]}!")
    print(f"{start2} {rhymes[i][1]}.")