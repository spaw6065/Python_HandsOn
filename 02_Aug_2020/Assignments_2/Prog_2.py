'''2) WAP to convert temperature from degree centigrade to Fahrenheit.
# Ex: (°C × 9/5) + 32 = °F'''

degree_cent_temp = float(input("Enter the degree centigrade temperature... :"))

def convert_celsius_to_fahrenheit(degree_cent_temp):
    degree_fah_temp = degree_cent_temp*(9/5)+32
    return round(degree_fah_temp,2)

def convert_fahrenheit_to_celsius(fahrenheit_temp):
    degree_celsius_temp = (5/9)*(fahrenheit_temp-32)
    return round(degree_celsius_temp,2)


print(f"Degree celsius temperature {degree_cent_temp} degree celsius and equivalent Fahrenheit temperature is {convert_celsius_to_fahrenheit(degree_cent_temp)} Fahrenheit")
print(f"Degree Fahrenheit temperature {convert_celsius_to_fahrenheit(degree_cent_temp)}  Fahrenheit and equivalent Fahrenheit temperature is {convert_fahrenheit_to_celsius(convert_celsius_to_fahrenheit(degree_cent_temp))} degree celsius")