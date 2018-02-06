# coding=utf-8
# 存储要用到的所有 URL

BASE_URL = "http://lol.766.com/db/lol/"

#地区
REGION_URL = BASE_URL + "agendaCmpEvent?area=1"

#队员简要信息列表
def get_play_list_url(areaId, prefix):
    return  BASE_URL + "player/list?areaId=" + areaId + "&prefix=" + prefix

#队伍简要信息列表
def get_team_list_url(areaId):
    return  BASE_URL + "team/list?areaId=" + areaId

#全球总排名
ALL_WORLD_RANK_URL = BASE_URL + "api/rank/"

#总-战队地区排行 //一般一页排完所以：
def get_team_rank_url(areaId):
    return  BASE_URL + "rank/teamList?orderType=1&orderKey=score&page=1&size=20&areaId=" + areaId

#LPL联赛战队榜
def get_team_rank_main(rankId):
    return BASE_URL + "competitionEvent/" + rankId + "/heroRanking?page=1&orderKey=bpRate&orderType=1&stageId=&areaId="

#LPL联赛选手榜
def get_team_rank_player(rankId):
    return BASE_URL + "competitionEvent/" + rankId + "/playerRanking?page=1&orderKey=displayScore&orderType=1&stageId=&areaId=&gamePositionId="

#LPL联赛英雄榜
def get_team_rank_legend(rankId):
    return BASE_URL + "competitionEvent/" + rankId + "/heroRanking?page=1&orderKey=bpRate&orderType=1&stageId=&areaId="

#LPL联赛积分榜
def get_team_rank_score(rankId):
    return BASE_URL + "competitionEvent/" + rankId + "/leagueRank?orderKey=score"