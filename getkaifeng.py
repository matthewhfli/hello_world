# coding=utf-8
from BeautifulSoup import BeautifulSoup
import urllib2

url = 'http://www.sjhcx.com/city/henan/kaifeng.php'
#伪装浏览器头
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

req = urllib2.Request(url = url,headers = headers)
html = urllib2.urlopen(req).read()
soup = BeautifulSoup(html.decode('gb2312'))

print soup.findAll('a')
links = soup.findAll('a')

for link in links:
    print(link.text)

