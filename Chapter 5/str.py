print('Release the kraken! ' + 'No, wait!')
print("My word! " "A gentleman caller!")
print("Alas! ""The kraken!")

vowels = ('a'
"e" '''i'''
'o' """u"""
)
print(vowels)

a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a + b + c)
print(a, b, c)


start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)


letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])

# print(letters[100])

# name = 'Henny'
# name[0] = 'P'

name = 'Henny'
print(name.replace('H', 'P'))
print('P' + name[1:])


letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])

print(letters[18:-3])
print(letters[-6:-2])

print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])

print(letters[-1::-1])
print(letters[::-1])

print(letters[-50:])
print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])

print(len(letters))
empty = ""
print(len(empty))