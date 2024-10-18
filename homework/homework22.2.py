def prime_generator(n):
    for i in range(2,n):
        prime=True
        for j in range(2,int(i**0.5+1)):
            if(i%j==0):
                prime=False
                break
        if(prime):
            yield i


for prime in prime_generator(100):
    print(prime,end=", ")

