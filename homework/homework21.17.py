def kelvin_to_celsius(kelvin):
    return kelvin-273
def kelvin_to_fahrenheit(kelvin):
    return 9/5*(kelvin-273)+32
def celsius_to_fahrenheit(celsius):
    return 9/5*(celsius)+32
def celsius_to_kelvin(celsius):
    return celsius+273
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)/1.80
def fahrenheit_to_kelvin(fahrenheit):
    return 5/9*(fahrenheit-32)+273.15

dict={

        "kelvin to celsius":kelvin_to_celsius,
        "kelvin to fahrenheit":kelvin_to_fahrenheit,
        "celsius to fahrenheit":celsius_to_fahrenheit,
        "celsius to kelvin":celsius_to_kelvin,
        "fahrenheit to celsius":fahrenheit_to_celsius,
        "fahrenheit to kelvin":fahrenheit_to_kelvin

        }

def convert_temperature(value,unit):
    if unit in dict:
        return dict[unit](value)
    else:
        raise ValueError(f"Unsupported conversion from {unit}")


print(convert_temperature(25, "celsius to fahrenheit"))
print(convert_temperature(77, "fahrenheit to celsius")) 
print(convert_temperature(0, "celsius to kelvin"))
print(convert_temperature(273.15, "kelvin to fahrenheit")) 
