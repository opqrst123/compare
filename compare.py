# -*-coding:utf-8 -*-


from gensim import corpora, models, similarities
from globe_info import *
from xlrd import open_workbook
from xlutils.copy import copy
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def compare(id, title, first_content_path, second_content_path):

    first_file = open(first_content_path, 'r')

    first_list = []
    list2 = [first_list, ['123', '321']]
    for line in first_file.read().decode('utf-8').split():
        first_list.append(line)
    dictionary = corpora.Dictionary(list2)
    corpus = [dictionary.doc2bow(text) for text in list2]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    second_file = open(second_content_path, 'r')
    query = second_file.read().decode('utf-8')
    second_list = []
    for line in query.split():
        second_list.append(line)
    second_file.close()
    vecbow = dictionary.doc2bow(second_list)
    vec_tfidf = tfidf[vecbow]

    index = similarities.MatrixSimilarity(corpus_tfidf)
    sims = index[vec_tfidf]
    percent = list(sims)

    # a = open(result_path, 'a')
    # a.write('id=%s,%s,相似度：%s\n' % (id, title.encode('utf-8'), str(percent[0])))
    # a.close()

    rb = open_workbook(result_path, formatting_info=True)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(id, 0, str(id))
    sheet.write(id, 1, title)
    sheet.write(id, 2, str(percent[0]))
    wb.save(result_path)
    print('已保存第%s个比对结果' % str(id))