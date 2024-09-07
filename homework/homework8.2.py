#1
# str="capitalize"
#print(str.capitalize())

#2

str="capitalize"
if(str[0]>'a' and str[0]<'z'):
    newstr=chr(ord(str[0])-32)
    newstr=newstr+str[1:]
    print(newstr)
else:
    print(str)