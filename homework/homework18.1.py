def greet(firstname,lastname,message="Hello"):
    print(f"{message} {firstname} {lastname}")
firstname=input("Input your firstname ")
lastname=input("Input your lastname ")
greet(firstname,lastname)
greet(lastname=lastname,firstname=firstname,message="Wellcome")

