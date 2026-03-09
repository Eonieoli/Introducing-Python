# from datetime import date

# halloween = date(2019, 10, 31)
# print(halloween)
# print(halloween.day)
# print(halloween.month)
# print(halloween.year)

# print(halloween.isoformat())


# from datetime import date

# now = date.today()
# print(now)


# from datetime import timedelta

# one_day = timedelta(days=1)
# tomorrow = now + one_day
# print(tomorrow)
# print(now + 17*one_day)
# yesterday = now - one_day
# print(yesterday)


# from datetime import time

# noon = time(12, 0, 0)
# print(noon)
# print(noon.hour)
# print(noon.minute)
# print(noon.second)
# print(noon.microsecond)


# from datetime import datetime

# some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
# print(some_day)
# print(some_day.isoformat())


# from datetime import datetime

# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)


from datetime import datetime, time, date

noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)