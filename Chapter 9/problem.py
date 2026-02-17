# 1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())


# 2
def get_odds():
    for i in range(10):
        if i % 2 != 0:
            yield i

odds = get_odds()
# print(odds)

cnt = 0
for odd in odds:
    if cnt == 2:
        print(odd)
    cnt += 1


# 3
def test(func):
    def inner(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return inner

@test
def function_call():
    print("function call")

function_call()


# 4
class OopsException(Exception):
    pass

def oops():
    raise OopsException("뭔가 잘못되었습니다!")

try:
    oops()
except OopsException as e:
    print("Caught an oops:", e)