import  re
str ="cat,mat,sat,hat,rat,pat"
# word=re.findall('[h-m]at',str) #Finding series start from h to m
# for i in word:
#     print(i)

word=re.findall('[h-m]at',str) #Finding series apart from h to m
for i in word:
    print(i)
