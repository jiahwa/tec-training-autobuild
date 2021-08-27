#!/usr/bin/env python3
from os import walk, getcwd, path
from pathlib import PurePath

# ignore all of directories, include root level
IGNORE_DIRS = ['.git','bin','lib','include']

# ignore all files mathes
IGNORE_FILES = ['pyvenv.cfg','.DS_Store','.gitignore']

rootDir = getcwd()

result = []
for root, dir, files in walk(rootDir):
    dir.sort()
    files.sort()
    match = path.basename(root)
    if match in IGNORE_DIRS:
        dir[:] = [] # ignore sub
        continue;

    times = len(PurePath(root[len(rootDir)-1:]).parts)
    result.append('|\t' * (times-1) + '├── %s\n' %match)

    for fname in files:
        pre = '|\t' * times
        recordPos = pre
        if fname not in IGNORE_FILES:
            result.append(pre+'├── %s\n' %fname)
dirs = ''.join(result)

print(dirs)

