# coding=utf-8
import re
import functions
# import urladmin
#
# uset = urladmin.getallnoteurl()
# for b in uset:
#     print b

# import logging
# logging.basicConfig(format='%(asctime)s %(message)s', filename='info.log',level=logging.DEBUG)
# logging.info('good morning')


# phoneset = set()
# filename = "yichen.txt"
# with open(filename) as f:
#     content = f.read().splitlines()
#     for line in content:
#         #print line
#         l = re.findall('1[3|5|7|8|][0-9]{9}',line)
#         for e in l:
#             if e not in phoneset:
#                 phoneset.add(e)
#             print e
# print phoneset.__len__()

# import urllib2
# import json
# opener = urllib2.build_opener()
# #f = opener.open('https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13762096719')
# f = opener.open('https://www.baifubao.com/callback?cmd=1059&callback=phone&phone=18637130240')
#
#
# s = '*'+f.read()
#
# ss = s[s.index('('):]
# print ss
# #ss = '{"hello":"world","good":"morning"}'
# j = json.loads(ss)
# print j

# encodedjson = json.dumps(s)
# print encodedjson


# line = '手机：18349299386xyz18349299385'
# m = re.findall('1[3|5|7|8|][0-9]{9}',line)
# for e in m:
#     print e


filename = "yichen.txt"
with open(filename) as f:
    content = f.read().splitlines()
    for line in content:
        print line
        ps = functions.get_phones(line)
        for p in ps:
            print p