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
            print urlnote
            if urlnote not in urlnoteset:
                urlnoteset.add(urlnote)
    return urlnoteset

def getboardurl():
    urlhome = 'http://www.xx007.cn/'
    urlboardset = set()
    html = urllib2.urlopen(urlhome).read()
    html = html.decode('gbk')
    soup = BeautifulSoup(html)
    boardlist = soup.findAll('a',attrs={'href':re.compile('^index\.asp\?boardid=.*')})

    for board in boardlist:
        urlboard = urlhome+board['href']
        if urlboard not in urlboardset:
            urlboardset.add(urlboard)
    return urlboardset

def getallnoteurl():
    urlhome = 'http://www.xx007.cn/'
    urlnoteset = set()
    urlboardset = getboardurl()
    for urlboard in urlboardset:
        html = urllib2.urlopen(urlboard).read()
        html = html.decode('gb18030')
        soup = ""
        try:
            soup = BeautifulSoup(html)
        except:
            #print "erro exits here..."
            continue

        #找出板块内所有帖子(note)的页数
        tempstr = '';
        tds = soup.findAll('td',attrs={'class':'tabletitle1'})
        for i in range(len(tds)):
            if i==2:
                tempstr = tds[i].text
        page = int(tempstr[tempstr.index("/")+1:tempstr.index(u'页')])
        print page

        for i in range(1,page+1):
            if i>10:
                break
            url = urlboard + "&action=&topicmode=0&page=" + str(i)
            #print url
            if i == 1:
                listtitle = soup.findAll('div', attrs={'class':'listtitle'})
                for title in listtitle:
                    urlnote = urlhome + title.a["href"]
                    print urlnote
                    if urlnote not in urlnoteset:
                        urlnoteset.add(urlnote)
            if i > 1:
                html = urllib2.urlopen(url).read()
                html = html.decode('gb18030')
                soup = BeautifulSoup(html)
                listtitle = soup.findAll('div', attrs={'class':'listtitle'})
                for title in listtitle:
                    urlnote = urlhome + title.a["href"]
                    print urlnote
                    if urlnote not in urlnoteset:
                        urlnoteset.add(urlnote)
    return urlnoteset

#测试
# for url in getallurl():
#     print url




