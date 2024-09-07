def print_user_profile(first_name,last_name,*,age,city):
    print(f"First name:{first_name} {last_name}\nAge: {age}\nCity: {city}")
print_user_profile("John", "Doe", age=30, city="New York")    
