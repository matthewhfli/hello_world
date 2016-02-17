# coding=utf-8
import re




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


filename = "yichen.txt"
with open(filename) as f:
    content = f.read().splitlines()
    for line in content:
        phone = extract_phone(line)
        print phone
