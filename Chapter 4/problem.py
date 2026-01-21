# 4.1
secret = 5
guess = 4

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

# 4.2
small = True
green = False
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")