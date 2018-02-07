# coding=utf-8
from url_filter import *
from urllib import urlopen
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
        region.append(strs.encode("utf-8"))
    return region

#获取队员简要信息列表
def get_player_list_part(areaId, prefix):
    res = urlopen(get_play_list_url(areaId, prefix)).read().decode("utf-8")
    temp = json.loads(res.split("\n")[1])
    player = []
    for i in range(0,len(temp)):
        id = temp[i].get("id")
        #游戏ID
        name = temp[i].get("gameName")
        #队伍名称
        team = temp[i].get("teamName")
        #头像
        icon = temp[i].get("icon")
        #国旗
        region = temp[i].get("nationalityIcon")
        #国家ID
        regionId = temp[i].get("nationalityId")
        if regionId is None:
            strs = "{\"id\":" + str(id) \
                   + ",\"name\":\"" + name + "\"" \
                   + ",\"team\":\"" + team + "\"" \
                   + ",\"icon\":\"" + icon + "\"" \
                   + ",\"regionId\":" + str(0) \
                   + ",\"region\":\"" + region + "\"}"
        else:
            strs = "{\"id\":" + str(id) \
               + ",\"name\":\"" + name + "\"" \
               + ",\"team\":\"" + team + "\"" \
               + ",\"icon\":\"" + icon + "\"" \
               + ",\"regionId\":" + str(regionId) \
               + ",\"region\":\"" + region + "\"}"
        player.append(strs)
    return player

#获取队伍简要信息列表
def get_team_list_part(areaId):
    res = urlopen(get_team_list_url(areaId)).read().decode("utf-8")
    temp = json.loads(res.split("\n")[1])
    team = []
    for i in range(0,len(temp)):
        id = temp[i].get("id")
        name = temp[i].get("abbreviation")
        icon = temp[i].get("team_icon")
        all_name =  temp[i].get("name")
        strs = "{\"id\":" + str(id) \
               + ",\"name\":\"" + name + "\"" \
               + ",\"icon\":\"" + icon + "\"" \
               + ",\"all_name\":\"" + all_name + "\"}"
        team.append(strs)
    return  team
print get_team_list_part(1)
#总榜 - 766数据来源
def get_word_rank_part():
    pass

#--------战队四大属性--------

#LPL联赛战队榜
def get_team_rank_main_part():
    pass

#LPL联赛选手榜
def get_team_rank_player_part():
    pass

#LPL联赛英雄榜
def get_team_rank_legend_part():
    pass

#LPL联赛积分榜
def get_team_rank_score_part():
    pass