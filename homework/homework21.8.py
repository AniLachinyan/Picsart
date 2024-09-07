def make_greeting(greeting):

    def name_of_greeter(name):
        print(f"{greeting}, {name}!")
    return name_of_greeter

make_greeting("welcome")("Ann")
make_greeting("Hello")("Bob")


