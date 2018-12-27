import re
string="""
        Hello 
        this is python class
        You'r learning Regex
    """


regex=re.findall("\S",string)
print(string)
data=" ".join(regex)
print(data)
#\w [A-Za-z0-9]
#\W[^A-Za-z0-9]