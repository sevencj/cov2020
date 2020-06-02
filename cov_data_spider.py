import requests
import json


def get_data():
    url1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    url2 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    headers = \
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }

    res1 = json.loads(requests.get(url1, headers).text)  # json.loads 作用是将json字符串转换成字典
    # 疫情当日详细数据
    detail_data = json.loads(res1['data'])

    res2 = json.loads(requests.get(url2, headers).text)
    # 疫情每天最新情况
    chinaDaydict = json.loads(res2['data'])

    history = {}  # 历史数据
    # 每日最新总概况
    for i in chinaDaydict['chinaDayList']:
        # 日期
        dt = ('2020.' + i['date']).replace('.', '-')
        # 确诊人数
        confirm = i['confirm']
        # 疑似病例
        suspect = i['suspect']
        # 治愈人数
        heal = i['heal']
        # 死亡人数
        dead = i['dead']
        history[dt] = {'confirm': confirm, 'suspect': suspect, 'heal': heal, 'dead': dead}

    # 每日新增概况
    for i in chinaDaydict['chinaDayAddList']:
        # 日期
        dt = ('2020.' + i['date']).replace('.', '-')
        # 新增确诊
        confirm = i['confirm']
        # 新增疑似
        suspect = i['suspect']
        # 新增治愈
        heal = i['heal']
        # 新增死亡
        dead = i['dead']
        history[dt].update({'confirm_add': confirm, 'suspect_add': suspect, 'heal_add': heal, 'dead_add': dead})

    details = []
    # 最后更新时间
    update_time = detail_data['lastUpdateTime']
    # 中国
    data_country = detail_data['areaTree']
    # 中国34个省
    data_province = detail_data['areaTree'][0]['children']
    for pro_infos in data_province:
        # 省名
        province = pro_infos['name']
        for city_infos in pro_infos['children']:
            # 市区县名
            city = city_infos['name']
            # 确诊人数
            confirm = city_infos['total']['confirm']
            # 新增确诊
            confirm_add = city_infos['today']['confirm']
            # 治愈人数
            heal = city_infos['total']['heal']
            # 死亡人数
            dead = city_infos['total']['dead']
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    # print(details)
    return history, details


if __name__ == '__main__':
    history, details = get_data()
    print(history, '\n', details)


# # print(data_all['areaTree'][0].keys())
# print(data_all['areaTree'][0]['children'])
#
# for i in data_all['areaTree'][0]['children']:
#     print(i['today'])
# print(len(data_all['areaTree'][0]['children']))








