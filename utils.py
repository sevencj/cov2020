import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


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


def query(sql,*args):
    """、
    通用的查询方法
    :param sql:
    :param args:
    :return: 返回查询到的结果
    """
    conn, cusor = get_conn()
    cusor.execute(sql, args)
    res = cusor.fetchall()
    close_conn(conn, cusor)
    return res


def get_c1_data():
    sql = "select sum(confirm),"\
          "(select suspect from history order by ds desc limit 1),"\
          "sum(heal),"\
          "sum(dead) "\
          "from details "\
          "where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]


def get_c2_data():
    sql = "select province,sum(confirm) from details "\
          "where update_time=(select update_time from details "\
          "order by update_time desc limit 1)"\
          "group by province"
    res = query(sql)
    return res


def get_l1_data():
    sql = 'select ds,confirm,suspect,heal,dead from history'
    res = query(sql)
    return res


def get_l2_data():
    sql = 'select ds,confirm_add,suspect_add from history'
    res = query(sql)
    return res


def get_r1_data():
    sql = 'SELECT city,confirm FROM ' \
          '(select city,confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province not in ("湖北","北京","上海","天津","重庆") ' \
          'union all ' \
          'select province as city,sum(confirm) as confirm from details  ' \
          'where update_time=(select update_time from details order by update_time desc limit 1) ' \
          'and province in ("北京","上海","天津","重庆") group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    return res


def get_r2_data():
    sql = 'select content from hotspot order by id desc limit 20'
    res = query(sql)
    return res


if __name__ == '__main__':
    print(get_r2_data())

