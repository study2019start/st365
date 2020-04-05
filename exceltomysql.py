import xlrd
import asyncio
import datetime
import time 
import threading
from access import access_model
import os

queueLock = threading.Lock()
class thred(threading.Thread):
    def __init__(self,n,li,dbn):
        threading.Thread.__init__(self)
        self.name1=n   #
        self.li=li  #excel表的路径
        self.lie=[] #数据表的表名
        self.dbname=dbn #数据库名称
        
    def run(self):
        rs=xunh(self.name1,self.li)
        for i,rs1 in enumerate(rs):
            s= self.read_excel(rs1)
            self.accessup(s,str(self.li[i]).replace(".xls","").replace(".xlsx",""),self.dbname)


    def read_excel(self,filename):
        dataa = []
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0) #第一个sheet
        ra = sheet.nrows  #总行数
        na= sheet.ncols   #总列数
        for aa in range(0,na): 
            self.lie.append(sheet.cell_value(0,aa)) #获取第一行数据，数据表的表名
        for i in range(1,ra):#从第二行开始
            a=[]
            for s in range(0,na):#从第一列开始
                v = sheet.cell_value(i,s)
                a.append(v) #每一行的数据
            dataa.append(a)
        return dataa

    def accessup(self,s,tablename,dbn):
        mm=access_model(dbn)
        l1=[]
        l2=[]
        lis=self.lie[1:len(self.lie)] #数据表的名字除去第一列的列名
        for ss in s:  #每一行的数据
            dd={}
            id1={}
            for i,l in enumerate(lis):
                dd[l]=ss[i+1]  #列名和数据组成字典 数据从第二列开始
            id1[self.lie[0]]=str(ss[0])  #第一列的表名和数据组成字典用来查询
            l1.append(dd)
            l2.append(id1)
        #print(l1)
        queueLock.acquire()
        mm.update(l1,l2,tablename)#l1是更新数据，l2是where中的内容,table表名
        self.lie=[]
        queueLock.release()

async def readex(b,start):
    s=start+1000
    #mm = mysql_model()
    sheet1 = b.sheet_by_index(0)
    nrows = sheet1.nrows
    if s>nrows:
        s = nrows
    lis=[]
    for start in  range(start,s):
        s=()
        for o in range(1,9):
            s=s+(sheet1.cell_value(start,o),)
        lis.append(s)
    print(lis)
    #await pr(lis)
    #await mm.manyinsert(self.li,lis,"myappweb_cjdj_info")
    #mm.manyinsert(self.li,lis,"myappweb_cjdj_info")


def accessselectm(s,tablename,dbn):
    mm=access_model(dbn)
    res=mm.muselect(s,tablename)
    return res


async def pr(ss):
    end = time.time()
    s=end*1000
    i=str(s).find('.')
    d=str(s)[i:i+4]
    
    print(str(time.strftime("%H:%M:%S",time.localtime(end)))+" :"+str(d)+"--"+str(ss))
    
def xunh(n,li):
    ls=[]
    for lli in li:
        ls.append(os.path.join(n,lli))
    return ls
       

if __name__ == "__main__":
    t=time.time()
    #coo1=[0,1000,2000,3000,4000,5000]
    br=r'E:\工作\2019区段地价'
    r= []
    r2=[r'虹口—商业样点信息更新.xls']
    #r'静安—住宅样点价格信息更新1021.xls',r'静安—办公样点价格信息更新.xls',r'静安—商业样点价格信息更新1021.xls',
   # r'虹口—住宅样点信息更新.xls',r'虹口—商业样点信息更新.xls',r'虹口—办公样点信息更新1021.xls‘
    thread=[]
    t1=thred(br,r,"静安样点信息.mdb")
    t2=thred(br,r2,"虹口样点信息.mdb")
    t1.start()
    t2.start()
    thread.append(t1)
    thread.append(t2)
    for tt in thread:
        tt.join()
    #path=r"D:\21.xls"
    
    #b = xlrd.open_workbook(path)
    #readex(b,0)
    #tasks=[asyncio.ensure_future(readex(b,x)) for x in coo1]
    #loop=asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.wait(tasks))
    end=time.time()-t
    print(end)