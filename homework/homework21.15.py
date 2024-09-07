def uppercase(x):
    return x.upper()
def lowercase(x):
    return x.lower()
def titlecase(x):
    return x.title()
def reverse_string(x):
    return x[::-1]
dict={
        "uppercase":uppercase,
        "lowercase":lowercase,
        "titlecase":titlecase,
        "reverse":reverse_string
        }
def manipulate_string(x,operation):
    if operation in  dict:
        return dict[operation](x)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

print(manipulate_string("hello world","uppercase"))
print(manipulate_string("HELLO world","lowercase"))
print(manipulate_string("hello world","titlecase"))
print(manipulate_string("hello world","reverse"))

