import requests
import json
import csv

url2='https://www.reddit.com/r/news/controversial/.json?sort=controversial&t=all'
pot2='C:/Users/Julija/Desktop/prog1_projekt/news_con.csv'

url3='https://www.reddit.com/r/news/top/.json?sort=top&t=all'
pot3='C:/Users/Julija/Desktop/prog1_projekt/news_top.csv'

url4='https://www.reddit.com/r/worldnews/controversial/.json?sort=controversial&t=all'
pot4='C:/Users/Julija/Desktop/prog1_projekt/wnews_con.csv'

url5='https://www.reddit.com/r/worldnews/top/.json?sort=top&t=all'
pot5='C:/Users/Julija/Desktop/prog1_projekt/wnews_top.csv'

#vrne seznam novic iz jsona na tem url-ju in ID za naslednjo stran
def seznamnovic1(url):
    m=requests.get(url,headers={'User-agent': 'your bot 0.1'})
    podatki = json.loads(m.text,encoding='utf-8') ["data"]["children"]
    a=naredisezslo(podatki)
    naslednja=json.loads(m.text,encoding='utf-8') ["data"] ["after"]
    return (a,naslednja)

#POMOŽNIpretvori seznam slovarjev v manjši slovar(z manj podatki)
def naredisezslo(sez):
    seznam=[]
    for i in sez:
        a={'Naslov':0,'Score':0,'Komentarji':0,'Vir':0}
        a ['Naslov'] = i["data"] ['title']
        a ['Score']= i["data"] ['score']
        a ['Komentarji']=i["data"] ['num_comments']
        a ['Vir']=i ["data"]['domain']
        seznam.append(a)
    return seznam

#ustvari seznam slovarjev za 600 novic
def SEZNAMnovic(url):
    a='&after='
    head=seznamnovic1(url)
    sez=head[0]
    while len(sez)<600:
        head=seznamnovic1(url+a+head[1])
        sez=sez+head[0]
    else:
        return sez

#zapiše seznam slovarjev v csv    
def zapisi_tabelo(slovarji,pot):
    imena_polj=['Naslov','Score','Komentarji','Vir']
    with open(pot, 'w', encoding='utf-8') as csv_dat:
        writer = csv.DictWriter(csv_dat, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)
            
zapisi_tabelo(SEZNAMnovic(url2),pot2)
#zapisi_tabelo(SEZNAMnovic(url4),pot4)
#zapisi_tabelo(SEZNAMnovic(url3),pot3)
#zapisi_tabelo(SEZNAMnovic(url5),pot5)
