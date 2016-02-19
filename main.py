# coding=utf-8
import urladmin
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import functions

siglineset = set()
phoneset = set()

#加载siglineset
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

print "starting parse...."
for link in urladmin.getallurl():
    note = ""
    try:
        note = urllib2.urlopen(link).read()
    except:
        print "urlopen erro existiong here..."
        continue
    note = note.decode('gb18030')
    # print note
    notesoup = BeautifulSoup(note)
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
