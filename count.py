# -*- coding: utf-8 -*-
# @Author: Du Jun

import time
import pymysql

def count():
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123", db="hexun")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = "select count(id) from hexun"
    cursor.execute(sql)
    print(cursor.fetchone())
    conn.close()

if __name__ == '__main__':
    while True:
        count()
        time.sleep(3)

