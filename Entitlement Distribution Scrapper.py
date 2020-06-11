import requests
from bs4 import BeautifulSoup
import json

import urllib.request, urllib.parse, urllib.error
import ssl
import os
import re

def readAndConToJson(url,ctx):
    data = dict()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    data[soup.find(id="lbl7782AverageText").string.rstrip(':')] = soup.find(id="lbl7782Average").string
    data[soup.find(id="lblPara2Text").string.rstrip(':')] = soup.find(id="lblPara2").string
    data[soup.find(id="lblEntitlementText").string.rstrip(':')] = soup.find(id="lblEntitlement").string
    data[soup.find(id="lblPercentChangeText").string.rstrip(':')] = soup.find(id="lblPercentChange").string
    data[soup.find(id="lblDesignDischargeText").string.rstrip(':')] = soup.find(id="lblDesignDischarge").string
    detail = list()
    table = soup.find(id="gvEntitlements")
    heads = table.find_all("th")
    rows = table.find_all("tr")
    for row in rows:
        info = row.find_all("span")
        i = 0
        dictionary = dict()
        for td in info:
            dictionary[heads[i].string] = (td.string)
            i = i + 1
        if i > 0:
            detail.append(dictionary)
    data["details"] = detail
    title = soup.find(id="lblMainDesc").string
    title = re.findall("^Entitlement and Actual Distribution of (.+)", title)[0]
    dt = dict()
    dt[title] = data
    # convert into JSON:
    y = json.dumps(dt)
    # the result is a JSON string:
    #print(y)
    f = open(title + ".json", "w")
    f.write(y)
    f.close()
    return;

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
data = [
  ('__EVENTTARGET', ''),
  ('__EVENTARGUMENT', ''),
  ('__LASTFOCUS', ''),
  ('__VIEWSTATE', 'zHpv5YTGg8GAzOFekjBEVDJLzn894Bnw2lHCMb3E/li9qQq/noUVQebmCF2J5xWbFWgUeKjMre+inza5ue44Zi01Olz0qdgvyvATKZoKbyM/VtfozjEM8e2bWXNPkhyOevS0qe/UXiYoNR9TcVyzgIzvhopPFcVQNfL8Ugu5expO4oqEmz4JpCPrmX+LheS0Gd6+YeVIlTyJ/aX5Djsg0NKIHxVuuKTXgYu/PLwN1W1jywY8ZlVUvAqe41VLp6LWlII1pDxCXMUdTc9zyQu1S9zXPGjFz4WRVvbaCAgZrrn1TD7vPLlqQuc1HY8uaqmh3DWz7D8Y1I6UGzENl4QUq72Llzg36yefW08/4NaJPGNViPMTg2cP79Edl1VaVkfXWv6w7yiNvYs/6Waw0/iq0rRip0d+ZbXHuPV/Kl9uGkCBcat/lUsVnoZpTqWZQiCI963D4JXu0nbETZV0Gu0WjnCM9IMagx4aMTIMDHe5S+dETu8kEmgZkwSwuDcJF/WIiQ3yCSQuOIPEr3IrVRJ4FsXySSe+wr0M1uaezbvJALuPbe1S2A26AVl5tv/x1sz013FhzcMgo/vUh0Xpxh4T8rwRNOsqkOWBDBvsj3i9g8IUzJ1+I3Be8797zq83NDmewyLEt1gr/PgHVYdhsMukng=='),
  ('__VIEWSTATEGENERATOR', '071C45B6'),
  ('__EVENTVALIDATION', 'jcFNszRia/kD69TlmjWq4z9GUKn9Vp2PakoIAQcGgliYh1G5zvkx2/7PuwGxmiWQauHJZ7i4eDBpkmDEWm+JKsnxGQxnhzA6va6Sd+xYxkw2G9nba80TGtMlTrDAx+JqWbuJjT9lNbb/fgm1HpUZHKr5dFrYuvG0606yN6b63eVrEedbm9xSmMUN/E1aKeqraERe8mDcpqo2IrsEjAOeBMU4LmY/KWRlb17tT2Yq/nQ1gjW9viP+0YS2FQj594tE84tBoF1KKNP9ETBK26lZ/4w3/3mZAxeke/JfJfyN30oJtS6ZL+zGgGNNrmE/YEksR/U3FB9eDyJBloDkZ+KGxcNEKiADxVcPTZO6UR25B+ZGCUEHF8bwJwTF3yI2CDq/kbyQBWRN0FED+t10FsB04ab3lM2247WGt/rx2h74uPI='),
  ('ddlSeason', '1'),
  ('ddlYear', '2019'),
  ('btnSearch', 'Search'),
]
s2_5=  ('__EVENTVALIDATION', '925PdWUcTcogmMzPUTPWCZu0qkJ+qOpRRsacdNMfz3cE0lf1yPgjZBkkT6xY8oBJzmViCpY6Ak51237SPXyOujuFxVABHPZ0+1xirrrAyM3YjGFyVQHPXeWHDZSmGqBBUtELiLe0U4e1CpaqktEjw3/PKCZ5TxS6NyBvRqQ6mR+Wkse43u9S/7SO3e6g1nvExdH7MPhu5R8oglzVEmFZZKjoDcjXjxL7WMOiqXshexLlC6tu60cM0CTGZMQJr8pZYH3N8JGikqNtP1gn1qFu5fhCINNCfLbuE+DWPQwfMh16noqxOqHh8rQEcfABpslDpV2CVbyuRlXo7tWQM88YKDpZYGrG0l++sMpJO614omGEqRfjkXwq1UK0KXcNUt/ffrhAXqNIAyQbLIjabrVmmtB0OwBgpjpo3nCUPHMvhs8=')
s2_3=('__VIEWSTATE', 'f0p7IkYOvfOUkWUuaKYsce96khJJd4sYEMM2Odxtq+eh4jGaGIBZl+orl2eLqUPrySaHGQfLc+fwDAyxTAwLD8E/7Ctm4JygYR2gWM9tp2BktUeG6bGU1IOwu8BRNhaOjV4oP/XsyqUUo9YRfTEKgs8EY05MjcwXMfb/MPPFUEfxt8qBNTyVbkwWsykJVXOKP2knJX9L0xxgaTmKL9GVsFINLz3Ve5+9km0xd3OiN/90I67RdUqOg1++5ZZLrks1StLUsetkesf9PXxyhOmZb+hcBK1EDJUufHThf66T/+bgJV/PtQcReYS8WI8bebymXV++3qU70tKKKLs+n871+hID/7V5D4T+mJuUKPYV95XBdUVsMJDW/YPf5VllrqFW/57HJdVOT5cRX6bOo4icq6LMoUOZyHQNbPg+MtaBSNX9HqGdAIS+2jgay/RWK8wJElpsDJN12UAR24BFT2cRWIdDpOGptspP4XDQPjyYVQ2PuRbx2EkRVkIW8L2NsgRPTFR05/hwKHOPpNCd5jP4ReVWnKOdevsZnfg2AsRB+DZmQOa3lbxAX/igy10L7mzAKXCXVqZcW9CvMjir+dYKBg==')
url='https://wrmis.irrigation.punjab.gov.pk/Modules/PublicWebSite/SearchEntitlements.aspx'
seasons=[]
years=[]
response = requests.post(url, data=data)
html = response.text
soup = BeautifulSoup(html, "html.parser")
tagSelect=soup('select')
URLS=[]
for tag in tagSelect:
  if tag['name']=='ddlSeason':
    for t in tag('option'):
      seasons.append(t['value'])
  elif tag['name']=='ddlYear':
    for t in tag('option'):
      years.append(t['value'])
prefix='https://wrmis.irrigation.punjab.gov.pk/Modules/PublicWebSite/'

for season in seasons:
  data[6]=('ddlSeason', season)
  if(season == '2'):
    data[5]=s2_5
    data[3]=s2_3
  for y in years:
    data[7]=('ddlYear', y)
    response = requests.post(url, data=data)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
      if (tag.text == 'Detail'):
        str=tag['href']
        URLS.append(prefix+str)
for u in URLS:
    readAndConToJson(u,ctx)
