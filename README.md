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

## 实施计划
- 第一阶段 根据json文件自动生成目录结构

核心函数 createdir：读入单个目录路径输出创建文件夹和文件是否成功

核心函数 readJson：读入json文件的路径输出string-json格式数据

核心函数 transform：读入string-json格式数据输出python支持的格式

工具函数 compareDirec: 标准化字典对比函数，读入python支持的格式输出ztree经典目录树结构，如：
```json
{
    "name":"",
    "isParent":true,
    "children":[]
}
```

函数1
```py
/* @params {String} relactivePath
*  @return {Boolean}
*/
createdir
```
函数2
```py
/* @params {String} absolutePath
*  @return defaults {string}
*/
readJson
```
函数3
```py
/* @params {String} strData
*  @return {Boolean}
*/
transform
```


- 第二阶段 根据目录结构自动生成json文件
- 第三阶段 修改json文件目录同步调整