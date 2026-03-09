# 1
from datetime import date

now = "2026-03-09"
f = open("today.txt", 'w')
f.write(now)
f.close()


# 2
f = open("today.txt", 'r')
today_string = f.read()
f.close()


# 3
today = today_string.split('-')
print(today)


# 4
birthday = date(1995, 3, 22)
print(birthday)


# 5
fmt = "Your birthday was %A."
print(birthday.strftime(fmt))


# 6
from datetime import timedelta

one_day = timedelta(days=1)
print(birthday + one_day * 10000)