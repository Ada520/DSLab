import urllib
from urllib import urlopen
import re
from bs4 import BeautifulSoup

path = "C:\Users\Kevin\Google Drive\Ipython\Data Science Lab\Lab3\scrapedPDF\\"
url = "http://proceedings.mlr.press/v70/"
content = urllib.urlopen(url).read()
soup=BeautifulSoup(content,"html.parser")
html = soup.find_all(href=re.compile("http://.*17[a-z].pdf"))

#more sanity check
print html[0]['href']
for i in range(0,len(html)):
    pdf_url = html[i]['href']
    f = open(path + str(i)+".pdf", 'wb')
    pdf = urlopen(pdf_url)
    f.write(pdf.read())
    f.close()