# coding=utf-8
#编辑玩加赛事请求头
import urllib

REQUEST_URL = "http://www.wanplus.com/ajax/stats/list"

REQUEST_HEAD = {
    "Host":"www.wanplus.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded",
    "X-CSRF-Token":"1355910551",
    "X-Requested-With":"XMLHttpRequest",
    "Referer":"http://www.wanplus.com/lol/playerstats",
    "Content-Length":"4901",
    "Cookie":"wanplus_token=30e1be20ab7923630ac5f77c8219508b; wanplus_storage=lf4m67eka3o; wanplus_sid=241e847e68c9a48ffcfff427034a042c; wanplus_csrf=_csrf_tk_1355910551; gameType=2; wp_pvid=3106352599; wp_info=ssid=s7765162836; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1517971942; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1517973060",
    "Connection":"keep-alive"
}


def get_request_body_rows():
    REQUEST_FORM_DATA = {
        "_gtk":"1355910551",
        "draw":"1",
        "columns[0][data]":"order",
        "columns[0][name]":"",
        "columns[0][searchable]":"true",
        "columns[0][orderable]":"false",
        "columns[0][search][value]":"",
        "columns[0][search][regex]":"false",
        "columns[1][data]":"playername",
        "columns[1][name]":"",
        "columns[1][searchable]":"true",
        "columns[1][orderable]":"false",
        "columns[1][search][value]":"",
        "columns[1][search][regex]":"false",
        "columns[2][data]":"teamname",
        "columns[2][name]":"",
        "columns[2][searchable]":"true",
        "columns[2][orderable]":"false",
        "columns[2][search][value]":"",
        "columns[2][search][regex]":"false",
        "columns[3][data]":"meta",
        "columns[3][name]":"",
        "columns[3][searchable]":"true",
        "columns[3][orderable]":"false",
        "columns[3][search][value]":"",
        "columns[3][search][regex]":"false",
        "columns[4][data]":"appearedTimes",
        "columns[4][name]":"",
        "columns[4][searchable]":"true",
        "columns[4][orderable]":"true",
        "columns[4][search][value]":"",
        "columns[4][search][regex]":"false",
        "columns[5][data]":"kda",
        "columns[5][name]":"",
        "columns[5][searchable]":"true",
        "columns[5][orderable]":"true",
        "columns[5][search][value]":"",
        "columns[5][search][regex]":"false",
        "columns[6][data]":"attendrate",
        "columns[6][name]":"",
        "columns[6][searchable]":"true",
        "columns[6][orderable]":"true",
        "columns[6][search][value]":"",
        "columns[6][search][regex]":"false",
        "columns[7][data]":"killsPergame",
        "columns[7][name]":"",
        "columns[7][searchable]":"true",
        "columns[7][orderable]":"true",
        "columns[7][search][value]":"",
        "columns[7][search][regex]":"false",
        "columns[8][data]":"mostkills",
        "columns[8][name]":"",
        "columns[8][searchable]":"true",
        "columns[8][orderable]":"true",
        "columns[8][search][value]":"",
        "columns[8][search][regex]":"false",
        "columns[9][data]":"deathsPergame",
        "columns[9][name]":"",
        "columns[9][searchable]":"true",
        "columns[9][orderable]":"true",
        "columns[9][search][value]":"",
        "columns[9][search][regex]":"false",
        "columns[10][data]":"mostdeaths",
        "columns[10][name]":"",
        "columns[10][searchable]":"true",
        "columns[10][orderable]":"true",
        "columns[10][search][value]":"",
        "columns[10][search][regex]":"false",
        "columns[11][data]":"assistsPergame",
        "columns[11][name]":"",
        "columns[11][searchable]":"true",
        "columns[11][orderable]":"true",
        "columns[11][search][value]":"",
        "columns[11][search][regex]":"false",
        "columns[12][data]":"mostassists",
        "columns[12][name]":"",
        "columns[12][searchable]":"true",
        "columns[12][orderable]":"true",
        "columns[12][search][value]":"",
        "columns[12][search][regex]":"false",
        "columns[13][data]":"goldsPermin",
        "columns[13][name]":"",
        "columns[13][searchable]":"true",
        "columns[13][orderable]":"true",
        "columns[13][search][value]":"",
        "columns[13][search][regex]":"false",
        "columns[14][data]":"lasthitPermin",
        "columns[14][name]":"",
        "columns[14][searchable]":"true",
        "columns[14][orderable]":"true",
        "columns[14][search][value]":"",
        "columns[14][search][regex]":"false",
        "columns[15][data]":"damagetoheroPermin",
        "columns[15][name]":"",
        "columns[15][searchable]":"true",
        "columns[15][orderable]":"true",
        "columns[15][search][value]":"",
        "columns[15][search][regex]":"false",
        "columns[16][data]":"damagetoheroPercent",
        "columns[16][name]":"",
        "columns[16][searchable]":"true",
        "columns[16][orderable]":"true",
        "columns[16][search][value]":"",
        "columns[16][search][regex]":"false",
        "columns[17][data]":"damagetakenPermin",
        "columns[17][name]":"",
        "columns[17][searchable]":"true",
        "columns[17][orderable]":"true",
        "columns[17][search][value]":"",
        "columns[17][search][regex]":"false",
        "columns[18][data]":"damagetakenPercent",
        "columns[18][name]":"",
        "columns[18][searchable]":"true",
        "columns[18][orderable]":"true",
        "columns[18][search][value]":"",
        "columns[18][search][regex]":"false",
        "columns[19][data]":"wardsplacedPermin",
        "columns[19][name]":"",
        "columns[19][searchable]":"true",
        "columns[19][orderable]":"true",
        "columns[19][search][value]":"",
        "columns[19][search][regex]":"false",
        "columns[20][data]":"wardskilledPermin",
        "columns[20][name]":"",
        "columns[20][searchable]":"true",
        "columns[20][orderable]":"true",
        "columns[20][search][value]":"",
        "columns[20][search][regex]":"false",
        "order[0][column]":"4",
        "order[0][dir]":"desc",
        "start":"0",
        "length":"20",
        "search[value]":"",
        "search[regex]":"false",
        "area":"",
        "eid":"579",
        "type":"player",
        "gametype":"2",
        "filter":"{\"team\"%3A{}%2C\"player\"%3A{}%2C\"meta\"%3A{}}"
        }
    #py3使用 urllib.parse.urlencode(REQUEST_FROM_DATA)一步到位
    #可惜我是2.7
    rows = ""
    for i in REQUEST_FORM_DATA:
        rows = rows + str(i) + "=" + REQUEST_FORM_DATA[i] + "&"
    rows = urllib.quote(rows)
    return rows