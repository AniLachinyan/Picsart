def compose(f,g):

    return lambda x: f(g(x))

def f(x):
    return x*x+2

def g(x):
    return (x+x)*2

print(compose(f,g)(3))
