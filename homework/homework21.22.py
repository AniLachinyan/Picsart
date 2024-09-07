import math

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(x)

math_functions = {
    "square": square,
    "cube": cube,
    "square_root": square_root,
    "factorial": factorial
}

def math_operations(number, operation):
    if operation in math_functions:
        return math_functions[operation](number)
    else:
        raise ValueError(f"Unsupported math operation: {operation}")

# Example usage
print(math_operations(4, "square"))        # Output: 16
print(math_operations(3, "cube"))          # Output: 27
print(math_operations(16, "square_root"))  # Output: 4.0
print(math_operations(5, "factorial"))     # Output: 120

