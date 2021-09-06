# tec-training-autobuild
autobuild


```init.[lang].json
{
    "attrs": {
        "title": ""
    },
    "children":[{
            "attrs": { "title": "" },
            "children":[
                {
                    "attrs": {"title": "examples"},
                    "children": [
                        {"attrs": {"title": "","content": ""}}
                    ]},
                {
                    "attrs": {"title": "code"},
                    "children": [
                        {"attrs": {"title": "","content": ""}}
                    ]},
                {
                    "attrs": {"title": "exercises"},
                    "children": [
                        {"attrs": {"title": "","content": ""}}
                    ]}
            ]
        }]
}
```

## 运行
>运行前先安装python虚拟环境，参见 https://github.com/jiahwa/pycookbook/blob/master/starter/py.md
```
python ./src/stage1
```sh

## 实施计划
- 第一阶段 根据json文件自动生成目录结构

核心函数 createdir：读入单个目录路径，输出创建文件夹是否成功

核心函数 createfile：读入单个目录路径，输出创建文件是否成功

核心函数 readJSON：读入json文件的路径，输出string-json格式数据

核心函数 transform：读入string-json格式数据，输出python支持的格式

**工具函数 compareDirec: 标准化字典对比函数，读入任意json格式，输出ztree经典目录树结构(目前耦合度高，无法扩展任意格式)**

核心函数 traverse：读入python支持的格式数据，输出ztree经典目录树
如：
```json
{
    "name":"",
    "isParent":true,
    "children":[]
}

- 第二阶段 根据目录结构自动生成json文件

核心函数 walk: 读取指定目录生成ztree经典目录树结构
- 第三阶段 修改json文件目录同步调整