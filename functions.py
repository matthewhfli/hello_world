# coding=utf-8
import re
import urllib2
from BeautifulSoup import BeautifulSoup

def extract_phone(line):
    info_list = line.split('<br/>')
    name = ""
    phone = ""
    for e in info_list:
        if re.compile('姓名.*').match(e):
            name = e
            idx = name.find("（")
            #print idx
            if idx>0:
                name = name[0:idx]
        if re.compile('手机.*|电话.*').match(e) and re.compile('.*\d{11}').match(e) :
            m = re.search('1\d{10}',e)
            if m:
                phone = m.group()
    if phone !="":
        return phone


def get_phone(line):
    #print line
    phone=""
    info_list = line.split('<br/>')
    for e in info_list:
        if re.compile('电.*|固话.*|手机.*|电话.*|.*手机.*').match(e) and re.compile('.*1\d{10}').match(e) :
            m = re.search('1\d{10}',e)
            if m:
                phone = m.group()

    return phone

def get_phones(line):
    phoneset = set()
    info_list = line.split('<br/>')
    for e in info_list:
        if re.compile('电.*|固话.*|手机.*|电话.*|.*手机.*').match(e) and re.compile('.*1\d{10}').match(e) :
            l = re.findall('1[3|5|7|8|][0-9]{9}',e)
            for ee in l:
                if ee not in phoneset:
                    phoneset.add(ee)
                    #print e
    return phoneset

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
