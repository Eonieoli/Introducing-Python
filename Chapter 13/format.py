# import time

# now = time.time()
# print(time.ctime(now))


# import time

# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# t= time.localtime()
# print(t)
# print(time.strftime(fmt, t))


# from datetime import date

# some_day = date(2019, 7, 4)
# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# print(some_day.strftime(fmt))


# from datetime import time

# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# some_time = time(10, 35)
# print(some_time.strftime(fmt))


# import time

# fmt = "%Y-%m-%d"
# print(time.strptime("2019-01-29", fmt))


# import time

# fmt = "%Y-%m-%d"
# print(time.strptime("2019-01-29", fmt))

# # print(time.strptime("2019-13-29", fmt))


# import locale
# from datetime import date

# halloween = date(2019, 10, 31)
# for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(halloween.strftime('%A, %B %d'))


import locale

names = locale.locale_alias.keys()
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(good_names[:5])

de = [name for name in good_names if name.startswith('de')]
print(de)