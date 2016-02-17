# coding=utf-8
import re




def test_format_sign(line):
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
            m = re.search('\d{11}',e)
            if m:
                phone = m.group()
    if name !="" and phone !="":
        print name +"," +phone


filename = "yichen.txt"
with open(filename) as f:
    content = f.read().splitlines()
    for line in content:
        test_format_sign(line)
