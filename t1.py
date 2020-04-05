from test import s
import re


if  __name__ == "__main__":
    sst="dd十五万2019-20asd是"
    re4=r".*[\u4e00-\u9fa5](\d+-\d+)[a-z].*"
    ree=re.search(re4,sst)
    print(ree[1])
    
    