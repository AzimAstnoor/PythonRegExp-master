import re
randstr='''
Hello all
this is python class
today we learn RegEx
'''
print(randstr)
redex=re.compile("\n")
reandStr=redex.sub(" ",randstr)
print(reandStr)

#\b: backspace
#\f: Formfeed
#\r: Carriage returen
#\t: Tab
#\v: Vertical tab
