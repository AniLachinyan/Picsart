def max(ls):
    max=ls[0]
    for i in range(len(ls)):
        if(max<ls[i]):
            max=ls[i]
    return max
ls=[1,33,2,344,5667,12]
print("Maximum element is ",max(ls))

def min(ls):
    min=ls[0]
    for i in range(len(ls)):
        if(min>ls[i]):
            min=ls[i]
    return min
print("Minimum element is  ",min(ls))

