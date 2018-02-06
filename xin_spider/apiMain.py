# coding=utf-8
from url_filter import *
from urllib import urlopen,quote
import json

#获取地区信息
def get_region_part():
    res = urlopen(REGION_URL).read().decode("utf-8")
    temp = json.loads(res.split("\n")[1])
    list = temp.get("area")
    region = []
    for i in range(0,len(list)):
        id = list[i].get("id")
        name = list[i].get("name")
        icon = list[i].get("icon")
        strs = "{\"id\":"+str(id)+",\"name\":\""+name+ "\"" + ",\"icon\":\""+icon+"\"}"
        region.append(strs)
    return region
print(get_region_part())