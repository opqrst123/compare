# -*-coding:utf-8 -*-

import MySQLdb
from globe_info import *
from save_url import *
from split_to_word import *
from get_clean_content import *
from compare import *
import time


def get_url_info(saved_id):
        conn = MySQLdb.connect(host=mysql_info['host'], user=mysql_info['user'], passwd=mysql_info['passwd'],
                               db=mysql_info['db'], port=int(mysql_info['port']), charset='utf8')
        cur = conn.cursor()
        if str(saved_id) != '':
            sql1 = 'SELECT count(1) FROM `t_zzyq_news` where id>%s order by id asc' % saved_id
            sql2 = 'SELECT id,content,url,title FROM `t_zzyq_news` where id>%s order by id asc' % saved_id
        else:
            sql1 = 'SELECT count(1) FROM `t_zzyq_news` where id order by id asc'
            sql2 = 'SELECT id,content,url,title FROM `t_zzyq_news` where id order by id asc'

        cur.execute(sql1)
        count = cur.fetchone()
        print(count[0])
        cur.execute(sql2)
        result = cur.fetchall()
        conn.cursor().close()
        conn.close()
        for i in range(0, count[0]):
            id = result[i][0]
            content = result[i][1]
            url = result[i][2]
            title = result[i][3]
            # save_url(url)
            split_to_word(content, id, db_word_path)
            html_content = ''
            n = 0
            while html_content == '':
                html_content = get_clean_content(url)
                if html_content == '':
                    time.sleep(2)
                    print('%s的html_content为空，稍后重试' % str(id))
                n += 1
                if n == 3:
                    break
            split_to_word(html_content, id, html_word_path)

            first_path = db_word_path + '\\' + str(id) + '.txt'
            second_path = html_word_path + '\\' + str(id) + '.txt'
            compare(id, title, first_path, second_path)

            path = dirs+'\\id.txt'
            a = open(path, 'w')
            a.truncate()
            a.write(str(id))
            a.close()
