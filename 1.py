# # # import lxml.html,requests
# # # url ='https://www.python.org/dev/peps/pep-0020/'
# # # xpath ='//*[@id="the-zen-of-python"]/pre/text()'
# # # res = requests.get(url)
# # # ht = lxml.html.fromstring(res.text)
# # # text = ht.xpath(xpath)
# # # print("hello!\n"+" ".join(text))

# # import bs4, requests
# # from bs4 import BeautifulSoup

# # # bs1 = BeautifulSoup(ht.cotent, 'html.parser')
# # # bs.find(href = "https://book.douban.com").text

# # bs1 = BeautifulSoup('<b>this is comment</b>')
# # print(type(bs1.find('b').string))
# # print(bs1.find('b').string)

# # import requests
# # from bs4 import BeautifulSoup
# # import re

# # ht = requests.get("https://www.douban.com")
# # bs1 = BeautifulSoup(ht.content, 'html.parser')

# # res = bs1.find(text=re.compile('热点内容'))

# # print(res.text)

# import pymysql.cursors
# import requests
# from bs4 import BeautifulSoup
# import arrow

# urls = ['https://news.so.com/ns?q=北京&pn={}&tn=newstitle&rank=rank&j=0&nso=10&tp=11&nc=0&src=page'.format(i) for i in range(10)]

# for i, url in enumerate(urls):
#     r = requests.get(url)
#     bs1 = BeautifulSoup(r.text)
#     parent_tag = bs1.find_all('li', class_='full-txt res-list pure-txt')

#     t_list = []
#     for one in parent_tag:
#         t_item = []
#         one_tag = one.find('a')
#         t_item.append(one_tag.get('href'))
#         t_item.append(one_tag.get('title'))

#         connection = pymysql.connect(host = 'localhost',
#                                      user = 'scraper1',
#                                      password = 'password',
#                                      db = 'DBS',
#                                      charset='utf8',
#                                      cursorclass=pymysql.cursors.DictCursor)
        
#         try:
#             with connection.cursor() as cursor:
#                 for one in t_list:
#                     try:
#                         sql_q = "INSERT INTO 'newspost' ('post_title', 'post_url', 'news_postdate',) VALUES (%s, %s, %s)"
#                         cursor.execute(sql_q, (one[1], one[0], one[2]))
#                     except pymysql.err.IntegrityError as e:
#                         print(e)
#                         continue

#                     connection.commit()

#         finally:
#             connection.close()
#         # print(one_tag.get('href'))
#         # print(one_tag.get('title'))
#         # website_tag = one.get('data-url')
#         # content_tag = one.find('div', class_ = 'g-txt-inner g-ellipsis')
#         # print(website_tag)
#         # print(content_tag.text)

import pickle

l1 = [1,3,5,7]
with open('l1.pkl', 'wb') as f1:
    pickle.dump(l1, f1)

with open('l1.pkl', 'rb') as f2:
    l2 = pickle.load(f2)
    print(l2)


