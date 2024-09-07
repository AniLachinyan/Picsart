count=int(input("Input count of people "))
ls=[]
for i in range(count):
    dict={}
    dict["Name"]=input("Input name ")
    dict["Surname"]=input("Input surname ")
    dict["ID"]=input("Input ID ")
    dict["E-mail"]=input("Input E-mail ")
    dict["Phone number"]=input("Input phone number ")
    ls.append(dict)
name=input("Enter the name you are searching ")
found=False
for i in range(count):
    if(ls[i]["Name"]==name):
        found=True
        for j, k in ls[i].items():
            print(j,k)    
if  not found:
    print("No people like that ")



