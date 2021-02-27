import urllib.request,re

def getPlazas():
    formatedData=list()
    with urllib.request.urlopen("https://de.wikipedia.org/wiki/Liste_der_Pl%C3%A4tze_in_M%C3%BCnchen") as url:
        data=url.read().decode("utf-8")
        filteredData = filter(lambda x: "<td>" in x and "</td>\n<td>" in x, data.split("<tr>"))
        filteredData = map(lambda x: re.findall("<td>.*</td>",x),filteredData)
        for i in filteredData:
            if len(i)!=5:
                if len(i)==0:continue
            i=list(map(lambda x:x[4:-5],i))
            i[0]=re.split("<br />",i[0])
            d={"type":"plaza"}
            if i[0][0][:2]=='<a':
                i[0][0]=i[0][0][i[0][0].find(">")+1:-4]
                d["url"]="/wiki/"+i[0][0].replace(" ","_")
            d["Name"]=i[0][0]
            d["Pos"]=i[0][1][i[0][1].find("href")+6:-len('">Lage</a></span>')]
            d["Stadtbezirk"]=i[1]
            d["Namensherkunkft"]=i[2]
            d["Jahr"]=i[3]
            if i[4]!='':
                d["Weitere Informationen"]=i[4]
            formatedData.append(d)
    return formatedData
