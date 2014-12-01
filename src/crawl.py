#encoding:UTF-8
import urllib2
import sys
import urllib

reload(sys)
sys.setdefaultencoding('utf8')
url = "http://www.csd.uwo.ca"

data={}
data['word']='HIT'
url_values=urllib.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values

data = urllib2.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)