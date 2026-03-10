# import os

# print(os.getpid())
# print(os.getcwd())

# print(os.getuid())
# print(os.getgid())


# import subprocess

# ret = subprocess.getoutput('date')
# print(ret)

# ret = subprocess.getoutput('date -u')
# print(ret)

# ret = subprocess.getoutput('date -u | wc')
# print(ret)

# ret = subprocess.check_output(['date', '-u'])
# print(ret)

# ret = subprocess.getstatusoutput('date')
# print(ret)

# ret = subprocess.call('date')
# print(ret)

# ret = subprocess.call('date -u', shell=True)

# ret = subprocess.call(['date', '-u'])


# import os

# print(os.uname())
# print(os.getloadavg())
# print(os.cpu_count())


# import os

# print(os.system('date -u'))


import psutil

# print(psutil.cpu_times(True))

# print(psutil.cpu_percent(True))

# print(psutil.cpu_percent(percpu=True))