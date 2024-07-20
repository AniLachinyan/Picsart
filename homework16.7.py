def reverse_str(string):
    if not string:
        return ""
    return reverse_str(string[1:])+string[0]
string=input("Enter your string ")
k=reverse_str(string)
print(f"reversed string is-> {k}")
