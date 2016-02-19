# coding=utf-8

import urllib2
from BeautifulSoup import BeautifulSoup
import re
import functions


boardid = str(16)
urlhome = 'http://www.xx007.cn/'
siglineset = set()
phoneset = set()

#init.加载siglineset
filename = "yichen.txt"
with open(filename) as f:
    content = f.read().splitlines()
    for line in content:
        #print line
        siglineset.add(line)
#加载phoneset
file_phone = "phone.txt"
with open(file_phone) as f:
    content = f.read().splitlines()
    for line in content:
        phoneset.add(line)
#板块
urlboard = 'http://www.xx007.cn/index.asp?boardid='+boardid
html = urllib2.urlopen(urlboard).read()
html = html.decode('gbk')
#print html
soup = BeautifulSoup(html)

#找出板块内所有帖子(note)的页数
tempstr = '';
tds = soup.findAll('td',attrs={'class':'tabletitle1'})
for i in range(len(tds)):
    if i==2:
        tempstr = tds[i].text
page = int(tempstr[tempstr.index("/")+1:tempstr.index(u'页')])
print page

for i in range(1,page+1):
    print "第"+str(i)+"页开始...."
    url = urlhome + "index.asp?boardid=" + boardid + "&action=&topicmode=0&page=" + str(i)
    #http://www.xx007.cn/index.asp?boardid=166&action=&topicmode=0&page=2
    print url
    html = urllib2.urlopen(url).read()
    html = html.decode('gb18030')
    soup = BeautifulSoup(html)
    listtitle = soup.findAll('div', attrs={'class':'listtitle'})

    for title in listtitle:
        link = urlhome + title.a["href"]
        print link
        note = urllib2.urlopen(link).read()
        note = note.decode('gb18030')
        #print note
        notesoup = BeautifulSoup(note)
        #帖子的第一页
        siglines = notesoup.findAll('div',attrs={'style':'width:85%;overflow-x: hidden;'})
        for sigline in siglines:
            strsigline = str(sigline)
            strsigline=strsigline[strsigline.index('<img'):]
            strsigline="".join(strsigline.split())
            if strsigline not in siglineset:
                siglineset.add(strsigline)
                print strsigline
                myfile = open(filename,'a+')
                myfile.write(strsigline+"\n")
                myfile.close()
            myphone = functions.get_phone(strsigline)
            if myphone not in phoneset:
                phoneset.add(myphone)
                print myphone
                thefile = open(file_phone,'a+')
                thefile.write(myphone+"\n")
                thefile.close()
        #帖子的其他页
        uurls = notesoup.findAll('a',attrs={'href':re.compile('^dispbbs.*')})
        if len(uurls):
            uurls.pop()
            for u in uurls:
                otherurl = urlhome + u["href"]
                print "otherurl:"+otherurl
                othernote = urllib2.urlopen(otherurl).read()
                othernote = othernote.decode('gb18030')
                othersoup = BeautifulSoup(othernote)
                siglines = othersoup.findAll('div',attrs={'style':'width:85%;overflow-x: hidden;'})
                for sigline in siglines:
                    strsigline = str(sigline)
                    strsigline=strsigline[strsigline.index('<img'):]
                    strsigline="".join(strsigline.split())
                    if strsigline not in siglineset:
                        siglineset.add(strsigline)
                        print strsigline
                        myfile = open(filename,'a+')
                        myfile.write(strsigline+"\n")
                        myfile.close()
                    myphone = functions.get_phone(strsigline)
                    if myphone not in phoneset:
                        phoneset.add(myphone)
                        print myphone
                        thefile = open(file_phone,'a+')
                        thefile.write(myphone+"\n")
                        thefile.close()