# encoding: UTF-8
import re
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'.*ello')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')
if match:
# 使用Match获得分组信息
    print match.group()
### 输出 ###
# hello
s = "0371-68198348059386,0871-33226688"
s2 = "ade"
p = re.compile('^\d{4}-\d{8}|\d{4}-\d{8}$')
p2= re.compile('abe|ade')
m = re.match(p2,s2)
if m:
    print m.group()


def testsearchandmatch():
  s1="helloworld, i am 30 !"

  w1 = "world"
  m1 =  re.search(w1, s1)
  if m1:
    print("find : %s" % m1.group())

  # if re.match(w1, s1) == none:
  #   print("cannot match")

  w2 = "helloworld"
  m2 = re.match(w2, s1)
  if m2:
    print("match : %s" % m2.group())
testsearchandmatch()
#find : world
#cannot match
#match : helloworld