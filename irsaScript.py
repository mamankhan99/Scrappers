
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='http://pakirsa.gov.pk/DailyData.aspx'
domainUrl='http://pakirsa.gov.pk/'
#add your local pc address where you want to store images
localAddr="\\pdf"
#check if the given
if not os.path.isdir(localAddr):
    os.makedirs(localAddr)
localAddr=localAddr+"\\"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup.find_all('a',href=re.compile("\ADoc/Data\S*pdf"))
for tag in tags:
    doc=str(tag.get('href', None))
    docUrl=domainUrl+doc
    location=localAddr+re.findall("(Data\S*.pdf)",doc)[0]
    if os.path.exists(location):
        continue
    urllib.request.urlretrieve(docUrl, location)

    #print(location)

