import re
str="Hinal,Cat,Rat,Pat,Sat,Mat"
word=re.findall('\w{5}',str)#in brackets define which word should be start
for i in word:
    print(i)