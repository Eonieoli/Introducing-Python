# 6.1
# for x in [3, 2, 1, 0]:
#     print(x)

# 6.2
# guess_me = 7
# number = 1

# while number <= guess_me:
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print("found it!")
#         break
#     else:
#         print("oops")
#         break
#     number += 1

# 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break