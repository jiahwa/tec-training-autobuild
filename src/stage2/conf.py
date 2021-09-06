#!/usr/bin/env python3
from os import walk, getcwd, path

# ignore all of directories, include root level
IGNORES = ['.git','bin','lib','include',
            'pyvenv.cfg','.DS_Store']
ROOTDIR = '/Users/yujiahua/GitHub/GitLab/fresh-grad-2021-train'

def walkdir():
    # pointer = [] # pointer
    result = []
    for root, dir, files in walk(ROOTDIR):
        # sort
        dir.sort()
        files.sort()

        match = path.basename(root)
        if match in IGNORES:
            dir[:] = [] # ignore sub
            continue
    
        # get childinfo
        childinfo = {"name": match, "isParent": "true", "children": []}
        # if pointer == []:
            # result.append(childinfo)
        result.append(childinfo)
        # else:
        #     for (index, dname) in enumerate(pointer):
        #         if  match == dname["name"]:
        #             childinfo = pointer[index]
        #             break
        # dir traverse
        for d in dir:
            dinfo = {"name": d, "isParent": "true", "children": []}
            childinfo["children"].append(dinfo)
            
        # get pointer
        # pointer = childinfo["children"]
        
        # files traverse
        for fname in files:
            fileinfo = {"name":fname, "isParent": "true"}
            childinfo["children"].append(fileinfo)
  
    return result

def main():
    result = walkdir()
    print(result)