import pymysql
from cov_data_spider import get_data
import time
import traceback
from hotsearch_spider import get_hot_topic


def get_conn():
    """连接mysql"""
    # 创建连接
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='scorpiocheng123',
                           db='cov2020')
    # 创建游标对象，
    cursor =conn.cursor()
    # 返回链接对象和游标对象
    return conn, cursor


def close_conn(conn, cursor):
    # 关闭游标
    if cursor:
        cursor.close()
    # 关闭链接
    if conn:
        conn.close()


def update_details():
    """更新 details表"""
    try:
        # 获取详细数据列表
        li = get_data()[1]
        # 获取链接对象，游标对象
        conn, cursor = get_conn()
        sql = 'insert into details(update_time, province, city, confirm, confirm_add, heal, dead) values (%s, %s, %s, %s, %s, %s, %s)'
        sql_query = ' select %s=(select update_time from details order by id desc limit 1)'  # 对比当前最大时间戳
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f'{time.asctime()}-->details开始更新数据')
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f'{time.asctime()}-->details更新数据完毕')
        else:
            print(f'{time.asctime()}-->details已是最新数据')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insert_history():
    """插入历史数据"""
    try:
        # 获取历史数据字典
        dic = get_data()[0]
        print(f'{time.asctime()}-->开始插入历史数据')
        conn, cursor = get_conn()
        sql = 'insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        for k, v in dic.items():
            cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'), v.get('suspect'),
                                 v.get('suspect_add'), v.get('heal'), v.get('heal_add'),
                                 v.get('dead'), v.get('dead_add')])
        conn.commit()
        print(f'{time.asctime()}-->历史数据输入成功')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history():
    """更新历史数据"""
    try:
        dic = get_data()[0]
        print(f'{time.asctime()}-->开始更新历史数据')
        conn, cursor = get_conn()
        sql = 'insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        sql_query = 'select confirm from history where ds=%s'
        for k, v in dic.items():
            if not cursor.execute(sql_query, k):
                cursor.execute(sql, [k, v.get('confirm'), v.get('confirm_add'), v.get('suspect'),
                                     v.get('suspect_add'), v.get('heal'), v.get('heal_add'),
                                     v.get('dead'), v.get('dead_add')])
        conn.commit()
        print(f'{time.asctime()}-->更新历史数据完毕')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_hot_topic():
    """更新热点数据"""
    try:
        hot_spot_list = get_hot_topic()
        print(f'{time.asctime()}开始更新热搜数据')
        conn, cursor = get_conn()
        sql = 'insert into hotspot(ds,content) values(%s,%s)'
        ts = time.strftime('%Y-%m-%d %X')
        for i in hot_spot_list:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f'{time.asctime()}数据更新完毕')
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == '__main__':
    update_hot_topic()
    update_details()
    update_history()

