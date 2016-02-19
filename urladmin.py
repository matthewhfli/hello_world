# coding=utf-8

import urllib2
from BeautifulSoup import BeautifulSoup
import re

def getallurl():
    print "programming is collecting urls,pls waiting..."

    urlhome = 'http://www.xx007.cn/'
    urlboardset = set()
    urlnoteset = set()

    html = urllib2.urlopen(urlhome).read()
    html = html.decode('gbk')
    soup = BeautifulSoup(html)
    boardlist = soup.findAll('a',attrs={'href':re.compile('^index\.asp\?boardid=.*')})

    for board in boardlist:
        urlboard = urlhome+board['href']
        if urlboard not in urlboardset:
            urlboardset.add(urlboard)

    for urlboard in urlboardset:
        #print urlboard
        html = urllib2.urlopen(urlboard).read()
        html = html.decode('gb18030')
        soup = ""
        try:
            soup = BeautifulSoup(html)
        except:
            #print "erro exits here..."
            continue
        listtitle = soup.findAll('div', attrs={'class':'listtitle'})
        for title in listtitle:
            urlnote = urlhome + title.a["href"]
            if urlnote not in urlnoteset:
                urlnoteset.add(urlnote)
    return urlnoteset

# for url in getallurl():
#     print url




