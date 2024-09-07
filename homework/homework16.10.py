def is_polindrom(n):
    if (len(n)==1):
        return True
    elif (n[0]!=n[-1]):
        return False
    else:
        return is_polindrom(n[1:-1])
k=input("enter string you want to check ") 
print(is_polindrom(k))    
