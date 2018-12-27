import re

line="Hello this is python class for RegEx Python"
for word in  re.findall('python',line,re.I):
    print(word)
