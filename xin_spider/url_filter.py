# coding=utf-8
# 存储要用到的所有 URL
#本项目因为一些问题使用 py2.7

BASE_URL = "http://lol.766.com/db/lol/"

#地区
REGION_URL = BASE_URL + "agendaCmpEvent?area=1"

#全球总排名
ALL_WORLD_RANK_URL = BASE_URL + "api/rank/"

#战队比赛
GAME_DICT = {
        #2016LPL区域预选赛
        "Regional_qualifier_16": 76,
        #2016LPL夏季赛升降级赛
        "Upgrade_class_16": 75,
        #2016LPL夏季赛
        "Summer_game_16": 62,
        #2016LPL春季赛
        "Spring_game_16": 51,
        #2015LPL区域预选赛
        "Regional_qualifier_15": 33,
        #2015LPL夏季赛
        "Summer_game_15": 32,
        #2015LPL春季赛
        "Spring_game_15": 30,
        #2014LPL夏季赛
        "Summer_game_14": 41,
        #2014LPL春季赛
        "Spring_game_14": 47,
    }

#队员简要信息列表
def get_play_list_url(areaId, prefix):
    return  BASE_URL + "player/list?areaId=" + str(areaId) + "&prefix=" + prefix

#队员详细信息列表
def get_play_info_url(xin_id):
    return BASE_URL + "api/player/" + str(xin_id)

#队伍简要信息列表
def get_team_list_url(areaId):
    return  BASE_URL + "team/list?areaId=" + str(areaId)

#总-战队地区排行 //一般一页排完所以：
def get_team_rank_url(areaId):
    return  BASE_URL + "rank/teamList?orderType=1&orderKey=score&page=1&size=20&areaId=" + str(areaId)

#LPL联赛战队榜
def get_team_rank_main(rankId):
    return BASE_URL + "competitionEvent/" + str(rankId) + "/teamRanking?page=1&orderKey=winRate&orderType=1&stageId=&areaId="

#LPL联赛选手榜
def get_team_rank_player(rankId):
    return BASE_URL + "competitionEvent/" + str(rankId) + "/playerRanking?page=1&orderKey=displayScore&orderType=1&stageId=&areaId=&gamePositionId="

#LPL联赛英雄榜
def get_team_rank_legend(rankId):
    return BASE_URL + "competitionEvent/" + str(rankId) + "/heroRanking?page=1&orderKey=bpRate&orderType=1&stageId=&areaId="

#LPL联赛积分榜
def get_team_rank_score(rankId):
    return BASE_URL + "competitionEvent/" + str(rankId) + "/leagueRank?orderKey=score"