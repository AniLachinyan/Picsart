def data(data,/,*,operation="sum"):
    if (operation=="sum"):
        return sum(data)
    elif (operation=="max"):
        return max(data)
    elif (operation=="min"):
        return min(data)
    else:
        return "Unsupported operation,You can use sum max or min "
print(data([1,3,4,5,6,7,8]))    
print(data([1,2,3,4,5,6,7],operation="max")) 
print(data([1,2,3,4,5,6,7],operation="min"))       
