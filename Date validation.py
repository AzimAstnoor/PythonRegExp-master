#12-12-2019
#12-Dec-2019

import re
data="Chandni has birthdate on 13-10-1994  Saurbh has birthdate on 15-12-2001"
name=re.findall("[A-Z]{1}[a-z]*",data)
bdate=re.findall("\d{2}-\d{2}-\d{4}",data)
zipObj=zip(name,bdate)
dictData=dict(zipObj)
print(dictData)
print(dictData["Chandni"])

a=dict()
x=0
for key in name:
    a[key]=bdate[x]
    x+=1
print(a)
