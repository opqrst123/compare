# compare
目的：比对爬虫结果与原网页内容的相似度

从mysql中获取爬虫结果的正文和url
获取每个url的正文
对正文进行中文分词
使用gensim对比2个文件的相似度
并保存到本地excel文件

1.1优化：
保存最新的进度，存储id到本地txt文件
中断后，从断点继续