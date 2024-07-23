def flatten_list(ls):
    if not ls:
        return []
    elif(isinstance(ls[0],list)):
        return flatten_list(ls[0])+flatten_list(ls[1:])
    return [ls[0]]+flatten_list(ls[1:])
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print(f"Flattened list is {flatten_list(nested_list)}")
