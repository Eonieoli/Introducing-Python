# import os

# os.mkdir('poems')
# print(os.path.exists('poems'))

# os.rmdir('poems')
# print(os.path.exists('poems'))

# os.mkdir('poems')
# print(os.listdir('poems'))

# os.mkdir('poems/mcintyre')
# print(os.listdir('poems'))

# fout = open('poems/mcintyre/the_good_man', 'wt')
# print(fout.write('''Cheerful and happy was his mood,
# He to the poor was kind and good,
# And he oft' times did find them food,
# Also supplies of coal and wood,
# He never spake a word was rude,
# And cheer'd those did o'er sorrows brood,
# He passed away not understood,
# Because no poet in his lays
# Had penned a sonnet in his praise,
# 'Tis sad, but such is world's ways.
# '''))
# fout.close()


# import os

# os.chdir('poems')
# print(os.listdir('.'))


# import glob
# print(glob.glob('m*'))

# print(glob.glob('??'))

# print(glob.glob('m??????e'))

# print(glob.glob('[klm]*e'))


# win_file = 'eek\\urk\\snort.txt'
# win_file2 = r'eek\urk\snort.txt'
# print(win_file)
# print(win_file2)


# import os

# print(os.path.abspath('oops.txt'))

# print(os.path.realpath('jeepers.txt'))


# import os

# win_file = os.path.join("eek", "urk")
# win_file = os.path.join(win_file, "snort.txt")

# print(win_file)


# from pathlib import Path

# file_path = Path('eek') / 'urk' / 'snort.txt'
# print(file_path)
# print(file_path.name)
# print(file_path.suffix)
# print(file_path.stem)


# from pathlib import PureWindowsPath

# print(PureWindowsPath(file_path))