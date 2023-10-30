import geopandas as gpd

desc = """
{
	"name":"buffer",
	"description":"得到缓冲区",
	"inputs":{
		"datafile":"要求缓冲区的数据文件",
		"radius":"缓冲区半径"
	},
    "output":"缓冲区结果文件"
}
"""

example = """
指令：修一条铁路，宽度为30米，需要计算铁路占用的面积；铁路数据是railway.shp。
json: [{
	"name":"buffer",
	"inputs":{
		"datafile":"railway.shp",
		"radius":15
	},
    "output":"railway_buffer.shp"
}]
"""

def buffer(datafile:str, radius:float, output:str):
    data = gpd.read_file(datafile)
    radius = float(radius) # 防止部分llm给出的是字符串
    result = data.buffer(radius)
    result.to_file(output)
    return output


