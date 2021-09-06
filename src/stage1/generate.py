#!/usr/bin/env python3
from os import makedirs,path
from shutil import rmtree
from json import loads

# all creating file types
FILE_TYPES = ['md','html','css','js','png','jpg']

ROOT = '/Users/yujiahua/GitHub/tec-training-autobuild/dist'
JSON = '/Users/yujiahua/GitHub/tec-training-autobuild/init.zh-cn.json'

def createdir(relactivePath:str, root=ROOT):
    # path test: day01
    absolutePath = path.join(root, relactivePath)
    makedirs(absolutePath)
    return True

def createfile(relactivePath:str, root=ROOT):
    # path test: day01
    absolutePath = path.join(root, relactivePath)
    f = open(absolutePath, 'w')
    f.close()
    return True
    
def mkfiles(ztree, pre=''):
    for dir in ztree["children"]:
        current_path = path.join(pre, dir["name"])
        if current_path.find('.') > -1:
            dot_pos = current_path.rindex('.')
            if current_path[dot_pos+1:] in FILE_TYPES:
                createfile(current_path)
        else:
            print(current_path)
            createdir(current_path)
            if dir["children"]:
                    mkfiles(dir, current_path)
                
def clear(absolutePath:str=ROOT):
    if path.exists(absolutePath):
        rmtree(absolutePath)
        makedirs(absolutePath)
    else:
        makedirs(absolutePath)
    return True

def readJSON(absolutePath:str=JSON):
    # path test: JSON
    fd = open(absolutePath,'r')
    content = fd.read()
    fd.close()
    return content

def transform(str_json:str):
    # JSON 解码为 Python 类型
    py_data = loads(str_json)
    return py_data

def traverse(current, parent={}):
    # temp
    ztree_temp = {}
    ztree_temp["name"] = current["attrs"]["title"]
    
    if "children" not in current or len(current["children"]) == 0:
        ztree_temp["isParent"] = "false"
    else:
        ztree_temp["isParent"] = "true"
    
    if "children" not in parent:
        parent["children"] = []
    if parent !={}:
        parent["children"].append(ztree_temp)
    
    if "children" in current:
        for child in current["children"]:
            traverse(child, ztree_temp)
    return  parent
# def compareDirec(py_data:object):
#     # compared filed
#     ztree_formate = [
#         {
#             "ztree-field": "name",
#             "user-field": "title",
#             "rule": "root.attrs.title"
#         },
#         {
#             "ztree-field": "children",
#             "user-field": "children",
#         },
#         {
#             "ztree-field": "isParent",
#             "user-field": '',
#             "rule": "'children' not in root or len(root['children'])==0"
#         }
#     ]
#     ztree_object = visit_data(py_data)
#     return ztree_object

def main():
    clear()
    str_json = readJSON()
    py_data = transform(str_json)
    ztree = traverse(py_data)
    # test
    # print(ztree)
    mkfiles(ztree)


