#Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9
def convert_fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

try:
    user_input = input("please enter the temperature in fahrenheit: ")
    fahrenheit = float(user_input)
    celsius = convert_fahrenheit_celsius(fahrenheit)
except ValueError:
    print("invalid number")
else:
    print(f"{fahrenheit} degrees Fahrenheit is {celsius: .2f} degrees Celsius")
finally:
    print("thank you for using the weather forecast app")