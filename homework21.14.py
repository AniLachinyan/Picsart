def multiplication(x,y):
    return x*y
def division(x,y):
    if(y!=0):
        return x//y
    else:
        raise ValueError("Cannot divide by 0")
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y

dict={"+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
        }
def calculate(operand1,operand2,operator):
    if operator in dict:
        return dict[operator](operand1,operand2)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

print(calculate(10,2,"+"))
print(calculate(5,3,"*"))
print(calculate(10,2,"/"))
