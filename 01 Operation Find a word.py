import re

#Finding first match
line="Hello this is a class for RegExp and your are learning Python"

if re.search("python",line,re.I):
    print("'python' word is in this line")
else:
    print("'python' word isn't in this line")
