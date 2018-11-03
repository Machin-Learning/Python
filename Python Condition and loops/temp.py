# 2. Write a Python program to convert temperatures to and 
# from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius 
# and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 
c = 60
f = 45
celsius_to_fahrenheit = (c * 9 // 5) + 32
fahrenheit_to_celsius = (f - 32) * 5 // 9
print(f'{c}°C is {celsius_to_fahrenheit} in Fahrenheit')
print(f'{f}°F is {fahrenheit_to_celsius} in Celsius')