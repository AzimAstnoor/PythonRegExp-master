# Getting number and text from variable
import re
NameAge='''
        Ashok's age 23 and Kiran's age 21
        Dharmil's 25 and Hardik's age 20
        '''
ages=re.findall(r'\d{1,3}',NameAge)
names=re.findall(r'[A-Z][a-z]*',NameAge)
ageDict={}
x=0

for name in names:
    ageDict[name] = ages[x]
    x+=1
print(ageDict)