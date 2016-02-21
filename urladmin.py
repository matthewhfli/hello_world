# coding=utf-8

import urllib2
from BeautifulSoup import BeautifulSoup
import re


def getboardurl():
    urlhome = 'http://www.xx007.cn/'
    urlboardset = set()
    html = urllib2.urlopen(urlhome).read()
    html = html.decode('gbk')
    soup = BeautifulSoup(html)
    boardlist = soup.findAll('a', attrs={'href': re.compile('^index\.asp\?boardid=.*')})

    for board in boardlist:
        urlboard = urlhome + board['href']
        if urlboard not in urlboardset:
            urlboardset.add(urlboard)
    return urlboardset


def getallnoteurl():
    urlhome = 'http://www.xx007.cn/'
    urlnoteset = set()
    urlboardset = getboardurl()
    for urlboard in urlboardset:
        print urlboard
        html = ""
        soup = ""
        try:
            html = urllib2.urlopen(urlboard,timeout=30).read()
            html = html.decode('gb18030')
            soup = BeautifulSoup(html)
        except:
            continue

        # 找出板块内所有帖子(note)的页数
        tempstr = '';
        tds = soup.findAll('td', attrs={'class': 'tabletitle1'})
        for i in range(len(tds)):
            if i == 2:
                tempstr = tds[i].text
        page = 0
        try:
            page = int(tempstr[tempstr.index("/") + 1:tempstr.index(u'页')])
        except:
            print "get page erro"
            continue
        print page

        for i in range(1, page + 1):
            if i > 3:
                break
            url = urlboard + "&action=&topicmode=0&page=" + str(i)
            # print url
            html=""
            soup = ""
            try:
                html = urllib2.urlopen(url,timeout=30).read()
                html = html.decode('gb18030')
                soup = BeautifulSoup(html)
            except:
                print "soup erro2"
                continue

            listtitle = soup.findAll('div', attrs={'class': 'listtitle'})
            for title in listtitle:
                urlnote = urlhome + title.a["href"]
                if urlnote not in urlnoteset:
                    urlnoteset.add(urlnote)
                    print urlnote
    return urlnoteset

