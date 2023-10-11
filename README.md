# gischain

## 简介
gischain是利用大语言模型的能力，用户只需要发出一条需要完成的任务的指令，gischain就可以自动执行相应的gis工具，并返回结果。
具体可参见 example.py 中的例子，注意请把key更换为自己的。

## 技术原理
gischain内部实现的技术原理为：
1. gischain预先定义把可能用到的gis工具，用json格式描述功能
2. 用户给出需要完成任务的指令
3. gischain通过构造好的提示词，把gis工具的描述信息和任务指令，一起发给大语言模型
4. 大语言模型按照规定的格式返回需要调用的工具列表及其运行参数
5. gischain解析大语言模型的返回结果，并逐一执行工具

## TODO LIST
1. 目前只和在线的chatglm/qwen-turbo/gpt4做了适配，后续会考虑和更多大语言模型做适配，包括本地部署的大语言模型
2. 目前只提供了少量gis工具作为例子，需要的话请自行实现更多工具
3. 考虑通过ReACT机制做更复杂的工具编排调用
4. 通过向量匹配或微调等方式，支持工具数量众多的情况（避免token超量）

## Q&A
Q，为什么不直接用langchain？  
A：做了尝试，发现在未使用ChatGPT的情况下，经常出现格式解析错误的情况，且很难定位修复，还不如参考langchain的思路自行实现。

Q，gdal 用 pip install gdal安装失败怎么办？  
A：换用 conda install gdal 可能就好了。

Q，提示openai没有ChatComletion属性，怎么办？  
A：这是因为openai的版本过低，需要升级到至少0.28.1。先 pip uninstall openai ,再 pip install openai即可。

## 版本说明
### v0.0.3
1. 增加对gpt4的支持
2. 增加栅格相关的空间算子
3. data目录下增加对应的栅格地形数据文件
4. 在gpt4的加持下，支持更加复杂的空间分析任务指令

### v0.0.2
1. 增加对通义千问的支持
2. 内部增加llm类，方便后续增加对更多大语言模型的支持
3. 基于各大语言模型对提示词输入的要求各不相同，把提示词的构造放到大语言模型之内

### v0.0.1
1. 走通基本逻辑，实现三个工具，以及三个简单步骤能完成的gis分析任务
2. 仅支持在线chatglm