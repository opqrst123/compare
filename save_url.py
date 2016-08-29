from globe_info import *

def save_url(url):
    path = dirs+'\\url.txt'

    a = open(path, 'a')
    a.write('%s\n' % url)
    a.close()