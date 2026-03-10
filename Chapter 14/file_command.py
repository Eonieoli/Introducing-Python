# import os

# print(os.path.exists('oops.txt'))
# print(os.path.exists('./oops.txt'))
# print(os.path.exists('waffles'))
# print(os.path.exists('.'))
# print(os.path.exists('..'))


# name = 'oops.txt'
# print(os.path.isfile(name))
# print(os.path.isdir(name))
# print(os.path.isdir('.'))

# print(os.path.isabs(name))
# print(os.path.isabs('C:/big/fake/name'))
# print(os.path.isabs('big/fake/name/without/a/leading/slash'))


# import shutil
# shutil.copy('oops.txt', 'ohno.txt')


# import os
# # os.rename('ohno.txt', 'ohwell.txt')


# import os

# os.link('oops.txt', 'yikes.txt')
# print(os.path.isfile('yikes.txt'))
# print(os.path.islink('yikes.txt'))

# os.symlink('oops.txt', 'jeepers.txt')
# print(os.path.islink('jeepers.txt'))


# import os
# os.chmod('oops.txt', 0o400)


# import stat
# os.chmod('oops.txt', stat.S_IRUSR)


# import os
# uid = 5
# gid = 22
# os.chown('oops', uid, gid)


import os
os.remove('oops.txt')
print(os.path.exists('oops.txt'))