# 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.replace(' m', ' M'))


# 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boomm! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print(f'Q: {questions[0]}')
print(f'A: {answers[0]}')
print()
print(f'Q: {questions[1]}')
print(f'A: {answers[1]}')
print()
print(f'Q: {questions[2]}')
print(f'A: {answers[2]}')
print()


# 5.3
print("""My kitty cat likes %s,
My kitty cat likes %s,
My kitty at fell on his %s And now thinks he's a %s""" % ('roast beef', 'ham', 'head', 'clam'))


# 5.4
letter = """
    Dear {salutation} {name},
    Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any
{animals}.

    Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.

    Thank you for your support.
    Sincerely,
    {spokesman}
    {job_title}"""

# 5.5
print(letter.format(salutation='a', name='b', product='c', verbed='d', room='e', animals='f', amount='g', percent='h', spokesman='i', job_title='j'))

# 5.6
a = 'duck'.capitalize()
b = 'gourd'.capitalize()
c = 'spitz'.capitalize()

print("%sy Mc%sface" % (a, a))
print("%sy Mc%sface" % (b, b))
print("%sy Mc%sface" % (c, c))

5.7
print('{0}y Mc{0}face'.format(a))
print('{0}y Mc{0}face'.format(b))
print('{0}y Mc{0}face'.format(c))

# 5.8
print(f"{a}y Mc{a}face")
print(f"{b}y Mc{b}face")
print(f"{c}y Mc{c}face")