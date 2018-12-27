import re
num="123 112    1234-12345 6781231231231"

data=re.match("\d{4}-\d{5}",num)
print(data)