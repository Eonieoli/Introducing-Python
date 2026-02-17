# def do_nothing():
#     pass

# do_nothing()


# def make_a_sound():
#     print('quack')

# make_a_sound()

# def agree():
#     return True


# if agree():
#     print('Splendid!')
# else:
#     print('That was expected.')


# def echo(anything):
#     return anything + ' ' + anything

# print(echo('Rumplestiltskin'))


# def commentary(color):
#     if color == 'red':
#         return "It's a tomato."
#     elif color == "green":
#         return "It's a green pepper."
#     elif color == 'bee purple':
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color " + color + "."
    
# comment = commentary('blue')
# print(comment)


# print(do_nothing())


# thing = None
# if thing:
#     print("It's some thing.")
# else:
#     print("It's no thing")

# thing = None
# if thing is None:
#     print("It's nothing")
# else:
#     print("It's something")


# def whatis(thing):
#     if thing is None:
#         print(thing, "is None")
#     elif thing:
#         print(thing, "is True")
#     else:
#         print(thing, "is False")

# whatis(None)
# whatis(True)
# whatis(False)

# whatis(0)
# whatis(0.0)
# whatis('')
# whatis("")
# whatis('''''')
# whatis(())
# whatis([])
# whatis({})
# whatis(set())
# whatis(0.00001)
# whatis([0])
# whatis([''])
# whatis(' ')


# def menu(wine, entree, dessert):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay', 'chicken', 'cake'))
# print(menu('beef', 'bagel', 'bordeaux'))

# print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
# print(menu('frontenac', dessert='flan', entree='fish'))


# def menu(wine, entree, dessert='pudding'):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay', 'chicken'))

# print(menu('dunkelfelder', 'duck', 'doughnut'))


# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)

# buggy('a')
# buggy('b')  # expect ['b']


# def works(arg):
#     result = []
#     result.append(arg)
#     return result

# print(works('a'))
# print(works('b'))


# def nonbuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)

# nonbuggy('a')
# nonbuggy('b')


# def print_args(*args):
#     print('Positional tuple:', args)

# print_args()
# print_args(3, 2, 1, 'wait!', 'uh...')


# def print_more(required1, required2, *args):
#     print('Need this one:', required1)
#     print('Need this one. too:', required2)
#     print('All the rest:', args)

# print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# print_args(2, 5, 7, 'x')
# args = (2, 5, 7, 'x')
# print_args(args)
# print_args(*args)


# def print_kwargs(**kwargs):
#     print('Keyword arguments:', kwargs)

# print_kwargs()
# print_kwargs(wine='merlot', entree='mutton', dessert='macarron')


# def print_data(data, *, start=0, end=100):
#     for value in (data[start:end]):
#         print(value)
# data = ['a', 'b', 'c', 'd', 'e', 'f']
# print_data(data)
# print_data(data, start=4)
# print_data(data, end=2)


# outside = ['one', 'fine', 'day']
# def mangle(arg):
#     arg[1] = 'terrible!'

# print(outside)
# mangle(outside)
# print(outside)


# def echo(anything):
#     'echo returns its input argument'
#     return anything

# def print_if_true(thing, check):
#     '''
#     Prints the first argument if a second argument is true.

#     The operation is:
#         1. Check whether the *second* argument is true.
#         2. If it is, print the *first* argument.
#     '''
#     if check:
#         print(thing)
    
# help(echo)

# print(echo.__doc__)


# def answer():
#     print(42)

# answer()


# def run_something(func):
#     func()

# run_something(answer)

# print(type(run_something))


# def add_args(arg1, arg2):
#     print(arg1 + arg2)

# print(type(add_args))


# def run_something_with_args(func, arg1, arg2):
#     func(arg1, arg2)

# run_something_with_args(add_args, 5, 9)


# def sum_args(*args):
#     return sum(args)

# def run_with_positional_args(func, *args):
#     return func(*args)

# print(run_with_positional_args(sum_args, 1, 2, 3, 4))


# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(4, 7))


# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % quote
#     return inner(saying)

# print(knights('Ni!'))


# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2

# a = knights2('Duck')
# b = knights2('Hasenpfeffer')
# print(type(a))
# print(type(b))

# print(a)
# print(b)

# print(a())
# print(b())


# def edit_story(words, func):
#     for word in words:
#         print(func(word))

# stairs = ['thud', 'meow', 'thud', 'hiss']

# def enliven(word):  # 첫 글자를 대문자로 만들고 느낌표 붙이기
#     return word.capitalize() + '!'

# edit_story(stairs, enliven)

# edit_story(stairs, lambda word: word.capitalize() + '!')


# print(sum(range(1, 101)))


# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step

# print(my_range)

# ranger = my_range(1, 5)
# print(ranger)

# for x in ranger:
#     print(x)

# for try_again in ranger:
#     print(try_again)


# genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
# print(genobj)
# for thing in genobj:
#     print(thing)


# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function


# def add_ints(a, b):
#     return a + b

# print(add_ints(3, 5))

# cooler_add_ints = document_it(add_ints) # 데커레이터 수동 할당
# print(cooler_add_ints(3, 5))


# @document_it
# def add_ints(a, b):
#     return a + b

# add_ints(3, 5)


# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function


# @document_it
# @square_it
# def add_ints(a, b):
#     return a + b

# print(add_ints(3, 5))


# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b

# print(add_ints(3, 5))