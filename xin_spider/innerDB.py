# coding=utf-8
from apiMain import *
import pymysql
import demjson

conn = pymysql.connect(host = 'localhost',user = 'root',password = '699307', db = 'lol', charset = 'utf8')
cur = conn.cursor()
cur.execute("USE lol")

#插入地区信息
def inner_region_part():
    sql = "INSERT INTO basedata_region(xin_id,name,icon) VALUES(%s,%s,%s)"
    list = get_region_part()
    for i in range(0,len(list)):
        temp = demjson.decode(list[i])
        cur.execute(sql,(temp['id'],temp['name'],temp['icon']))
        cur.connection.commit()

#插入队员简要信息
def inner_player_list_part():
    sql = "INSERT INTO basedata_player(xin_play_id,game_name,team_name,play_icon,xin_country_id,country_name)" \
          "VALUES(%s,%s,%s,%s,%s,%s)"
    nameList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    areaList = [1,2,3,4,5,6,7,8]
    for i in range(0,len(areaList)):
        for j in range(0,len(nameList)):
            list = get_player_list_part(areaList[i],nameList[j])
            print list
            for k in range(0,len(list)):
                temp = demjson.decode(list[k])
                cur.execute(sql, (temp['id'],temp['name'],temp['team'],temp['icon'],temp['regionId'],temp['region']))
                cur.connection.commit()
                print "### innnering :"+str(temp)
    print "End Inner"

#插入766招牌四宝
#插入LPL战队榜
def inner_team_rank_main_part():
    pass
#更新 -Main
try:
    #国家信息更新完毕
    #inner_region_part()
    #队员部分信息更新完毕
    #inner_player_list_part()
    inner_team_rank_main_part()
finally:
    cur.close()
    conn.close()