import math

def area_circle(radius):
    return math.pi*radius**2
def area_square(side):
    return side**2
def area_rectangle(length,width):
    return length*width
def area_triangle(base,height):
    return 0.5*base*height

dict={
        "circle":area_circle,
        "square":area_square,
        "rectangle":area_rectangle,
        "triangle":area_triangle

        }
def calculate_area(shape,**kwargs):
    if shape in dict:
        return dict[shape](**kwargs)
    else:
        raise ValueError(f"Unsupported shape {shape}")
print(calculate_area("circle", radius=5))
print(calculate_area("square", side=4))       
print(calculate_area("rectangle", length=5, width=3))
print(calculate_area("triangle", base=6, height=4))
