arr1=[14, 15, 32, 66]
arr2=[14, 15, 8, 32, 66]
st1=set(arr1)
st2=set(arr2)
st3={}
if(len(st1)>len(st2)):
    st3=st1-st2
else:
    st3=st2-st1
print(st3)    

