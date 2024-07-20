def each_charachter(string):
    if not string:
        return ""
    print(string[0])
    return each_charachter(string[1:])
str=input("input your string ")
each_charachter(str)
