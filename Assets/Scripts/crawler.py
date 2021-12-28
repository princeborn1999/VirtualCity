import urllib.request as req
url = "https://weather.com/zh-TW/coronavirus/l/4ba28384e2da53b2861f5b5c70b7332e4ba1dc83e75b948e6fbd2aaceeeceae3"
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    })

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find("span",class_="CovidCasesOverview--primaryCount--2PJsk CovidCasesOverview--count--3IvNu CovidCasesOverview--confirmed--f2iks")#尋找class為parent_CheNg 的span標籤
confirmed_case = titles.string
path = 'output.txt'
f = open(path,'w')
f.write(confirmed_case)
f.close()