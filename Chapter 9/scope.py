# animal = 'fruitbat'
# def print_global():
#     print('inside print_global:', animal)

# print('at the top level:', animal)
# print_global()


# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)

# change_and_print_global()


# def change_local():
#     animal = 'wombat'
#     print('inside change_local:', animal, id(animal))

# change_local()
# print(animal)
# print(id(animal))


# animal = 'fruitbat'
# def change_and_print_global():
#     global animal
#     animal = 'wombat'
#     print('after the change:', animal)

# print(animal)
# change_and_print_global()
# print(animal)


# animal = 'fruitbat' # 전역 변수
# def change_local():
#     animal = 'wombat'   # 지역 변수
#     print('locals:', locals())

# print(animal)
# change_local()
# print('globals:', globals())
# print(animal)


def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()