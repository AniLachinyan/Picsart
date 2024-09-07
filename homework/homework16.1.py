def func(n):
    if(n==0):
        return 1
    func(n-1)
    print(n)
func(5)    
