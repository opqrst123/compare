# -*-coding:utf-8 -*-

# from readability import Document
from goose import Goose
from goose.text import StopWordsChinese
from globe_info import *
import os


def get_clean_content(url):

    g = Goose({'browser_user_agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0) ', 'stopwords_class': StopWordsChinese}) #核心要有这句
    article = g.extract(url=url)
    content = article.cleaned_text[:2000]
    return content


