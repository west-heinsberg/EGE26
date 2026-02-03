from fnmatch import fnmatch

for val in range(8387,10**9,8387):
    if fnmatch(str(val), '*75?122*'):
        print(val, val // 8387)