# LOLScrapy
**优雅的使用 py2.7(3.5 ...走远了)**

想法源于-> [[英雄联盟数据计划] 最初计划和构想](http://stringair.xin/?p=824)
### 1、此部分的需求
  在大概调研了一下数据之后得出结论，得先获取数据，而当下有完整数据的有：
   >* [766星竞界](http://lol.766.com/tour/47) 此间包含了2014 春季赛到2016年的区预选赛的战队数据，其中涵盖面非常广泛，包括战队总体信息，对战详细情况，英雄使用情况等多种。
   >* [玩加赛事](http://www.wanplus.com/lol/teamstats) 该网站更是丧心病狂，从S1到现在的数据都有，但是只包括战队KDA，选手的KDA，不包括详细对阵的英雄选择。
   >* [官方赛事中心](http://lpl.qq.com/es/data/) 是英雄联盟官方网站提供的数据平台，从战队-选手个人-再到英雄，做了详细的统计，但是也不存在详细的对阵情况，而更可惜的是只有2016-2017两年的数据。

   大概做完调研之后对目标也有了一定的方向，此部分作为基础数据的更新，暂时会分战队/个人/英雄的方式来采集LPL职业联赛以及S系列赛事的数据。

### 2、该部分的实现
  	调研后决定从766和玩家赛事两个部分下手 开搞，项目已创建
	766星竞界由于数据是自己通过 API 来获取的，所以接口外漏。。然后很简单，766这边的数据我用来直接拉取存库就好了

#### 1.766星竞界数据拉取[选手数据有效期至2017-夏季赛转会期前（韦酱还没有退役嘤嘤嘤）]
    （原来有766个选手信息。这也太草率了(╯‵□′)╯︵┻━┻）
    地区编号 ：http://lol.766.com/db/lol/agendaCmpEvent?area=1
 - 队员简要信息列表：http://lol.766.com/db/lol/player/list?areaId=&prefix= *[其中地区id在上面，prefix指首字母，取值a-z]*
 - ​队伍简要信息列表：http://lol.766.com/db/lol/team/list?areaId=1 *[地区id你懂得]*
 - 总-Rank：http://lol.766.com/db/lol/api/rank/ 
 - 总-地区排行：http://lol.766.com/db/lol/rank/teamList?orderType=1&orderKey=score&page=1&size=20&areaId=1 *[参数没做详细的查探和修正]*
 - LPL联赛战队榜 http://lol.766.com/db/lol/competitionEvent/47/teamRanking?page=1&orderKey=winRate&orderType=1&stageId=&areaId=  *[参数填少会有很多信息，在拉表 的时候详细查看]*
 - LPL联赛选手榜 http://lol.766.com/db/lol/competitionEvent/47/playerRanking?page=1&orderKey=displayScore&orderType=1&stageId=&areaId=&gamePositionId=
 - LPL联赛英雄榜 http://lol.766.com/db/lol/competitionEvent/47/heroRanking?page=1&orderKey=bpRate&orderType=1&stageId=&areaId=
 - LPL联赛积分榜 http://lol.766.com/db/lol/competitionEvent/47/leagueRank?orderKey=score
    1. 其中 competitionEvent 后面的数字指 对应的联赛
    2. 包含一个用途不明的URL http://lol.766.com/db/lol/competitionEvent/47/intro
  >* 2016LPL区域预选赛    76
  >* 2016LPL夏季赛升降级赛 75
  >* 2016LPL夏季赛  62
  >* 2016LPL春季赛 51
  >* 2015LPL区域预选赛 33
  >* 2015LPL夏季赛 32  
  >* 2015LPL春季赛 30
  >* 2014LPL夏季赛 41
  >* 2014LPL春季赛  47

#### 2.玩加赛事数据拉取[全方位的数据，但是没有图文并茂，我觉得很普通]
	由于发觉这里玩加赛事使用Ajax来请求数据，但是并没有API给暴露出来，这里有两条路可以走：
	  1. 要么使用Scrapy采集[暴力但通用]，
	  2. 要么尝试伪装成浏览器来请求他list的URL（这里是个坑我还完全没搞清这个，不过暂时还不用管，先去做上面的那个，完事再说）

 - 这里发觉玩加赛事的数据通过POST请求来提交，且有个巨长巨大的表单，请求头set-cookie。
    -（想截个图，结果这会访问不到了。不管了，先修正部分的数据）
 - 我使用简单的办法做了一部分的尝试
### 3、更新日志
`2018-02-06`
> - 创建项目  更新方式Log 更新部分信息到DB

`2018-02-07`
> - 更新玩家赛事部分采集块，设置部分请求头，部分情况未知
> - 已完成召唤师部分信息更新，和一些异常处理办法 远程主机DB创建完毕

`2018-02-26`
> - 过完年完善了队伍信息，开了新项目

### 4、问题
- 766的东西很怪。。杰克辣舞都来了，可是无状态还在NB。。*[等拉到玩家赛事的在修正一下]*
- 一个人写 任务量有点大。。我觉得还是先冷却冷却再说。。靠
- 测试Github 的公钥

