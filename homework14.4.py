fs=open("peterrabbit.txt",mode="r")
x=fs.read()
print(x)
text=x.split()
countexample=0
countall=0
countword=0
countup=0
countdid=0
counthim=0


for i in text:
    if(i=="example"):
        countexample+=1
    elif(i=="all"):
        countall+=1
    elif(i=="word"):
        countword+=1
    elif(i=="up"):
        countup+=1
    elif(i=="did"):
        countdid+=1
    elif(i=="him"):
        counthim+=1
print("count of example is",countexample)
print("count of all is",countall) 
print("count of word is",countword) 
print("count of up is",countup)   
print("count of did is",countdid)
print("count of him is",counthim)   
        

