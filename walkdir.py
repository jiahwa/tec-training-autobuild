#!/usr/bin/env python3
from os import walk, getcwd, path
from pathlib import PurePath
from string import Template

TITLE='2021应届生培训'
VERSION='_v1.1.1_'

# ignore all of directories, include root level
IGNORE_DIRS = ['.git','bin','lib','include']

# ignore all subs of directories, exclude root level

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

# Template
temp = Template('# $title\n\n$version\n\n文档结构说明：\n```\n$dirs```')
result = temp.substitute(title=TITLE, version=VERSION,dirs=dirs)

# write into file
f=open('README.md', 'w')
f.write(result)
f.close()

