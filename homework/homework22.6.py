def repeat_element(element,times):
    for i in range(times):
        yield element


for value in repeat_element(5,3):
    print(value)

for value in repeat_element("hiii",8):
    print(value)
for value in repeat_element([1,2,3,5],3):
    print(value)
    
