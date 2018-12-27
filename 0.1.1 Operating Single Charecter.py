import re
num="12345"
num2="123 1234 12345 123456 1234567"
print("Matches:",len(re.findall("\d",num))) #Matches the number
print("Matches:",len(re.findall("\D",num))) #Matches except the number
print("Matches:",len(re.findall("\d{4}",num))) #Matches particuler the number

print("Matches:",len(re.findall('\d{5,7}',num2)))#Matches the range of number
