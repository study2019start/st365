import requests
from bs4 import *
import random
import re

class Soufang(object):
    def __init__(self,loulist):
        self.lou=loulist
        self.re1=r"[\u4e00-\u9fa5]+"
        self.re2=r"(\d{4})年(\d{1,2})月(\d{1,2})日"
        self.re3=r".*([^\d{4}-]\d{2,3}-\d{1,4})+.*"
        self.re4=r".*(\d{2,3}-\d{1,4})+.*"
    def souf(self):
        dd={}
        dd['city']='上海'
        resultlist=[]
        ls=['','','','','']
        he={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','content-encoding':'gzip'}
        head={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
        url='https://sh.newhouse.fang.com/house/ajaxrequest/search_keyword_submit.php?t='+rand()
        for lo in self.lou:
            dd['keyword'] = lo
            result=requests.post(url,data=dd,headers=head)
            sp=result.text.split("^")
            if sp[0]=='100':
                url1='https:'+sp[1]+ '?xf_source='+lo
                print(url1)
                result2=requests.get(url1,headers=he)
                result2.encoding='gb2312'
                soup=BeautifulSoup(result2.text,"html.parser")
                w3=soup.select('div[id="orginalNaviBox"] >a')[1]['href']
                rs3=requests.get('https:'+w3,headers=he)
                rs3.encoding='gb2312'
                soup=BeautifulSoup(rs3.text,"html.parser")
                so=soup.select('div[class="main-item"] > ul[class="list clearfix"] > li >div')
                for i,soupr in enumerate(so):
                    if str(soupr.string).find("装修状况")>-1:
                        str1 = so[i+1].string
                        str2=''
                        res1 = re.findall(self.re1,str(str1))
                        if res1:
                            str2=res1[0]
                        ls[1]=str2
                        print(str2)
                        #replace('	','').replace('		',''))
                    elif str(soupr.string).find("开盘时间：")>-1:
                        str2=''
                        str1= str(so[i+1])
                        res1=re.findall(self.re2,str1)
                        if  res1:
                            if len(res1[0])>2:
                                str2=res1[0][0]+"-"+res1[0][1]+"-"+res1[0][2]
                        ls[0]=str2
                        print(str2)
                so=soup.select('div[class="main-item"] > div[class="main-table"] > div[class="table-part"] > table >tr >td')
                for sof in so:
                    res3=re.search(self.re3, str(sof))
                    if res3:
                        ree=res3.group(1)
                        print(ree)
                        re4=re.search(self.re4,str(ree))
                        if re4:
                            rs4=re4.group(1)
                            ls[1]=ls[1]+rs4+'㎡'
                            ls[2]=str(sof)
                            print(rs4+"  "+str(sof))
                            break
                resultlist.append(ls)
                
                ls=['','','','','']
            print(resultlist)

                    



            


    
def rand():
    return str(random.randint(1000000000000000,9999999999999999)/10000000000000000)

if __name__ == "__main__":
    lists=["招商虹桥公馆","保利云上"]
    sf=Soufang(lists)
    sf.souf()
    pass
