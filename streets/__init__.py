import urllib.request,re

def getStreets():
    formatedData = list()
    with urllib.request.urlopen("https://de.wikipedia.org/wiki/Liste_M%C3%BCnchner_Stra%C3%9Fennamen") as data:
        urldata = data.read().decode("utf-8")
        urldata = re.findall(r"/wiki/Liste_M%C3%BCnchner_Stra%C3%9Fennamen/[A-Z]%E2%80%93[A-Z]|/wiki/Liste_M%C3%BCnchner_Stra%C3%9Fennamen/[A-Z]",
                             urldata)
        urls = map(lambda x: x.split("\"")[0].strip("'"),urldata)
    for url in urls:
        with urllib.request.urlopen('https://de.wikipedia.org'+url) as data:
            filteredData=data.read().decode("utf-8")
            filteredData=filteredData[filteredData.find('<div class="toccolours noprint"')+4415:filteredData.find('<h2><span class="mw-headline" id="Einzelnachweise')]
            filteredData=re.split("<p><b>|<p><i>",filteredData)
            filteredData=map(lambda x:list(filter(lambda y:y!='</p>' and y!='',x)),map(lambda x:re.split("[\r\n]+",x),filteredData))
            for i in filteredData:
                d= {'type':'street'}
                i[0]=list(filter(lambda x:x!='',re.split(',[ ]*',i[0])))
                d["name"]=i[0][0][:-4]
                d["Historische Straße"]=(i[0][0][-2]=='i')
                if len(i[0])>=2:
                    d["url"]=i[0][1][9:]
                    d["url"]=d["url"][:d["url"].find('"')]
                    d["Stadtbezirk"]=i[0][1][i[0][1].find('>')+1:]
                    d["Stadtbezirk"]=d['Stadtbezirk'][:d['Stadtbezirk'].find('<')]
                if len(i)==1:
                    yield d
                    continue
                d['Jahr(e)']=i[1][i[1].find('(')+1:i[1].find(')')]
                d["Zusatzinformationen"]=i[1][i[1].find(')')+2:]
                yield d

if __name__ == "__main__":
    getStreets()