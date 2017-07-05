import requests
import lxml.html

for num in range(13):
 response = requests.get('http://www.keyakizaka46.com/s/k46o/diary/member/list?ct=10&page='+str(num))
 root = lxml.html.fromstring(response.content)
 links = root.cssselect('.box-ttl a')
 for a in links:
  title = a.text.encode('utf-8')
  print title
