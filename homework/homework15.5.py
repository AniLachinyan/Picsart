def first_upper_letter(n):
    for i in n:
        if(i.isupper()):
            return i
string="hellowOrld"
print("first upper letter ->", first_upper_letter(string))
