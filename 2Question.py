# Temperature Convertor Program
# Step-1 Taking input from user
temperature = float(input("Please Enter the temperature you want to convert:"))
unit = input("Is this temperature is Celsius or Fahrenheit? (C/F):").strip().upper()

# Step-2 Use the condition to determine Conversion direction
if unit == 'C':
    # Celsius to Fahrenheit
    # F = (C*9/5)+ 32
    fahrenheit = (temperature*9/5)+32
    print(f"{temperature}\u00B0 C is {round(fahrenheit)} in Fahrenheit")
elif unit == 'F':
    # Fahrenheit to Celsius
    # C = (F-32) *5/9
    celsius = (temperature -32) *5/9 
    print(f"{temperature}\u00B0 F is {round(celsius)} in Celsius")
else:
    print=  ("Invalid unit! Please Enter 'C' for Celsius and 'F' for Fahrenheit.")  
    
 
    
