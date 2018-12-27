import re
str="hello this is python class to RegEx"
for i in re.finditer("python",str):
    loctup=i.span()
    print(loctup)