def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def filter_list(lst, predicate):
    return list(filter(predicate, lst))

def map_list(lst, func):
    return list(map(func, lst))

list_operations = {
    "sort": sort_list,
    "reverse": reverse_list,
    "filter": filter_list,
    "map": map_list
}

def transform_list(lst, operation, *args):
    if operation in list_operations:
        if operation in ["filter", "map"]:
            if len(args) != 1:
                raise ValueError(f"{operation.capitalize()} requires exactly one argument.")
            return list_operations[operation](lst, args[0])
        else:
            return list_operations[operation](lst)
    else:
        raise ValueError(f"Unsupported list operation: {operation}")

# Example usage
print(transform_list([4, 2, 7, 1, 9], "sort"))
print(transform_list([4, 2, 7, 1, 9], "reverse"))
print(transform_list([4, 2, 7, 1, 9], "filter", lambda x: x > 3))
print(transform_list([4, 2, 7, 1, 9], "map", lambda x: x * 2))

