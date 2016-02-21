# coding=utf-8
import urladmin
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import functions

urlhome = 'http://www.xx007.cn/'
siglineset = set()
phoneset = set()

# 加载siglineset
filename = "yichen.txt"
with open(filename) as f:
    content = f.read().splitlines()
    for line in content:
        # print line
        siglineset.add(line)
# 加载phoneset
file_phone = "phone.txt"
with open(file_phone) as f:
    content = f.read().splitlines()
    for line in content:
        phoneset.add(line)

print "starting parse...."

for link in urladmin.getallnoteurl():
    print link
    note = ""
    try:
        note = urllib2.urlopen(link).read()
        note = note.decode('gb18030')
    except:
        continue

    # print note
    notesoup = ""
    try:
        notesoup = BeautifulSoup(note)
    except:
        continue
    # 帖子的第一页
    siglines = notesoup.findAll('div', attrs={'style': 'width:85%;overflow-x: hidden;'})
    for sigline in siglines:
        strsigline = str(sigline)
        strsigline = strsigline[strsigline.index('<img'):]
        strsigline = "".join(strsigline.split())
        if strsigline not in siglineset:
            siglineset.add(strsigline)
            print strsigline
            myfile = open(filename, 'a+')
            myfile.write(strsigline + "\n")
            myfile.close()
        myphone = functions.get_phone(strsigline)
        if myphone not in phoneset:
            phoneset.add(myphone)
            print myphone
            thefile = open(file_phone, 'a+')
            thefile.write(myphone + "\n")
            thefile.close()
    # 帖子的其他页
    uurls = notesoup.findAll('a', attrs={'href': re.compile('^dispbbs.*')})
    if len(uurls):
        uurls.pop()
        for u in uurls:
            otherurl = urlhome + u["href"]
            print otherurl
            othernote = ""
            try:
                othernote = urllib2.urlopen(otherurl).read()
                othernote = othernote.decode('gb18030')
            except:
                print "urlopen erro is here..."
                continue
            othersoup = ""
            try:
                othersoup = BeautifulSoup(othernote)
            except:
                print "othersoup erro"
                continue
            siglines = othersoup.findAll('div', attrs={'style': 'width:85%;overflow-x: hidden;'})
            for sigline in siglines:
                strsigline = str(sigline)
                strsigline = strsigline[strsigline.index('<img'):]
                strsigline = "".join(strsigline.split())
                if strsigline not in siglineset:
                    siglineset.add(strsigline)
                    print strsigline
                    myfile = open(filename, 'a+')
                    myfile.write(strsigline + "\n")
                    myfile.close()
                myphone = functions.get_phone(strsigline)
                if myphone not in phoneset:
                    phoneset.add(myphone)
                    print myphone
                    thefile = open(file_phone, 'a+')
                    thefile.write(myphone + "\n")
                    thefile.close()
