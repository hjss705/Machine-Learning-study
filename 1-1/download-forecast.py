import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId' : 108}

params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

date = urllib.request.urlopen(url).read()
text = date.decode("utf-8")
print(text)