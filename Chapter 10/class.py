# class Cat:
#     pass

# a_cat = Cat()
# print(a_cat)
# another_cat = Cat()
# print(another_cat)

# a_cat.age = 3
# a_cat.name = "Mr. Fuzzybuttons"
# a_cat.nemesis = another_cat

# print(a_cat.age)
# print(a_cat.name)
# print(a_cat.nemesis)

# # print(a_cat.nemesis.name)

# a_cat.nemesis.name = "Mr. Bigglesworth"
# print(a_cat.nemesis.name)


# class Cat:
#     def __init__(self):
#         pass


class Cat:
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')
print('Our latest addition:', furball.name)