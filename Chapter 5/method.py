tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
print(tasks.split())


crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)


setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous', 100))


world = " earth "
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())

print(world.strip('!'))

blurt = "What the...!!?"
print(blurt.strip('.?!'))


import string
print(string.whitespace)
print(string.punctuation)
blurt = "What the...!!?"
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))


poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

word = 'the'
print(poem.find(word))
print(poem.index(word))

word = 'the'
print(poem.rfind(word))
print(poem.rindex(word))

word = "duck"
print(poem.find(word))
print(poem.rfind(word))
# print(poem.index(word))
# print(poem.rindex(word))

word = 'the'
print(poem.count(word))

print(poem.isalnum())


setup = 'a duck goes into a bar...'
print(setup.strip('.'))

print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())


print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))