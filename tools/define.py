# from tools import buffer,overlay,calculateArea
import json

tools_mapping = {
    # "buffer": {"func":buffer,"dics":“{
    #                                     name:buffer,
    #                                     discription:得到缓冲区,
    #                                     inputs:{
    #                                         datafile:要求缓冲区的数据文件
    #                                         radius:缓冲区半径
    #                                         },
    #                                     output:缓冲区结果文件
    #                                 }”,
    # # "overlay": overlay,
    # "calculateArea": calculateArea,
}

from gischain import common

def call_tool(tool_name, node_name, result_dict, output, **kwargs):
    if tool_name in tools_mapping:
        func = tools_mapping[tool_name]["func"]
        print(f"开始运行工具 {tool_name} ，参数为：{kwargs}")
        # python只支持一个可变参数，这句话把output参数加上
        kwargs["output"] = output
        result = func(**kwargs)
        if result_dict != None:        
            common.update_kv_dict(result_dict, node_name, {"result":result})
            
        print(f"工具 {tool_name} 执行结束，输出为：{result}")
        return result
    else:
        print(f"没有找到名字为 {tool_name} 的工具")
        return None

import multiprocessing

def is_main_process():
    return multiprocessing.current_process().name == "MainProcess"

def add_tool(name, func, disc):
    tools_mapping[name] = {}
    tools_mapping[name]["func"] = func
    tools_mapping[name]["disc"] = disc
    # 仅在主进程中输出工具的初始化信息
    if is_main_process():
        print(f"初始化工具 {name} 成功，内容为：{disc}")

def get_tool_disc(name):
    if name in tools_mapping:
        function = tools_mapping[name]
        return function["disc"]
    else:
        print(f"没有找到名字为 {name} 的工具")
        return None
    
def get_tools_name():
    return list(tools_mapping.keys())