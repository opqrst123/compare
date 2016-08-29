# -*-coding:utf-8 -*-


from globe_info import *
import os
from get_url_info import *
import xlwt
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


if os.path.exists(dirs):
    print('文件夹已存在，不用新建')
else:
    os.makedirs(dirs)
    print('文件保存在%s' % dirs)


if os.path.exists(db_word_path):
    print('文件夹已存在，不用新建')
else:
    os.makedirs(db_word_path)
    print('分词文件保存在%s' % db_word_path)

if os.path.exists(html_word_path):
    print('文件夹已存在，不用新建')
else:
    os.makedirs(html_word_path)
    print('分词文件保存在%s' % html_word_path)


if os.path.exists(result_path):
    print("文件已存在，不需要新建")
else:
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    workbook.save(result_path)

if os.path.exists(id_path):
    print("文件已存在，不需要新建")
else:
    a = open(id_path, 'w')
    a.write('')
    a.close()

path = dirs+'\\id.txt'
a = open(path, 'r')
saved_id = a.read()
a.close()
print('id=%s ' % saved_id)
get_url_info(saved_id)


