import re
num=input("Enter your number:")
st="Hello my number is "+num
try:
    regex=re.findall("\d{3}-\d{3}-\d{4}",st)
    if(regex):
        print(num,"is valide")
    else:
        print(num,'is not valide')
except Exception as e:
    print("Exception",e)