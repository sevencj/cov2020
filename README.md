# cov2020
2020新冠病毒疫情实时追踪（中国地区）


总体流程
	一、爬取cov疫情数据
	
	二、爬取疫情热搜话题

	三、将获取到的数据入库（mysql）

	四、flask开发疫情数据追踪web



一、爬取cov疫情数据 （url：https://news.qq.com/zt2020/page/feiyan.htm#/?nojump=1）

1. 对网页进行分析 从抓包中发现数据的json文件  。

https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34108259100409239275_1591067543921&_=1591067543922
https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery34108259100409239275_1591067543923&_=1591067543924

2. 分析json数据结构，编写spider， 提取需要的数据。


二、爬取疫情热搜话题 （url：https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1）

1. 编写spider获取热搜话题（动态获取）

2. 通过selenium 模拟浏览器登录，点击， 获取数据等操作


三、将获取到的数据入库（mysql）

1. get_conn() 创建链接和游标

2. update_details 更新details数据 

先查询mysql最新的时间与获取的数据时间对比，如果库中时间大于等于获取时间则无需更新，反之更新

3. insert_history 插入history数据（只需运行一次）

4. update_history 更新history数据（只更新数据库中没有的数据，通过日期做比较）

5. update_hot_topic 更新热点数据 每次获取的数据都入库


四、flask开发疫情数据追踪web

1. pycharm创建flask项目

2. app.py 设置路由route

3. controller 定义 html function 

4. utils.py 封装功能
