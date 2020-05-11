
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import os
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='https://podaac-opendap.jpl.nasa.gov/opendap/GeodeticsGravity/tellus/L3/grace/land_mass/RL06/v03/CSR/contents.html'
prefix='https://podaac-opendap.jpl.nasa.gov/opendap/GeodeticsGravity/tellus/L3/grace/land_mass/RL06/v03/CSR/'

#add your local pc address where you want to store images
localAddr="\\img"
#check if the given
if not os.path.isdir(localAddr):
    os.makedirs(localAddr)
localAddr=localAddr+"\\"

html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup.find_all('a',itemprop="contentUrl",href=re.compile("tif"))
for tag in tags:
    img=str(tag.get('href', None))
    if img.endswith('tif'):
        url=prefix+img
        location=localAddr+img
        #dont download the file again if it already exists
        if os.path.exists(location):
            continue
        print(url)
        urllib.request.urlretrieve(url, location)
