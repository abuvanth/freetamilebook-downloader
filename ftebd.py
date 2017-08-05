import csv,os
import urllib
with open('all_files.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     with open('tmp.txt','w') as urls:     
          for row in spamreader:
              #print row[2]
              t=row[2]+'\n'
              urls.write(t)
urls.close()  
out=open('urls.txt','w')
with open('tmp.txt','r') as myfile:
     d=myfile.read()
     for i in d.split('\n'):
         if i.startswith("href='"):
            t=i[len("href='"):].split("/'>")
            out.write(t[0]+'\n')
out.close()
os.system('rm tmp.txt')
from bs4 import BeautifulSoup as bs
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'
}
z=1
#url='http://freetamilebooks.com/ebooks/poothathum-parithathum'
u=open('urls.txt','r')
for url in u.read().split():
    cont=requests.get(url,headers=headers)
    sp=bs(cont.text,'lxml')
    t=0
    for i in sp.find_all("a", class_="aligncenter download-button"):
        t=t+1
        if t==3:
           break
    ud=i.get('href')
    bn = ud.rsplit('/',1)[1]
    urllib.urlretrieve(ud,bn)
    print "download book",z
    z=z+1
