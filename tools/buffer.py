import geopandas as gpd

desc = """{
	"name":"buffer",
	"description":"得到缓冲区",
	"inputs":{
		"datafile":"要求缓冲区的数据文件",
		"radius":"缓冲区半径"
	},
    "output":"缓冲区结果文件"
}"""

example = """
指令：要计算加油站附近500米的区域，需要做缓冲区分析。加油站数据是gas_station.shp。
json: [{
	"name":"buffer",
	"inputs":{
		"datafile":"gas_station.shp",
		"radius":500
	},
    "output":"gas_station_buffer.shp"
}]"""

def buffer(datafile:str, radius:float, output:str):
    data = gpd.read_file(datafile)
    radius = float(radius) # 防止部分llm给出的是字符串
    result = data.buffer(radius)
    result.to_file(output)
    return output

from . import base
def check(tool):
    datafile = tool["inputs"]["datafile"]
    # 得到数据文件的后缀名
    if datafile.endswith('.shp') == False:
       return False, f"{datafile} 现在只支持shp文件；"
    return True, ""
    

