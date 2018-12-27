import re
str="cat,mat,sat,hat,rat,pat"
word=re.compile("rat")
replaceStr=word.sub("cat",str)
print(replaceStr)