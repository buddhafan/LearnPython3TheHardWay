#more variables and even more printing
name = 'Zed A. Shaw'
age = 35
height = 74 # inches
height_cm = height*2.54 
weight = 180 # lbs
weight_kg = weight * .453592
eyes = 'blue' 
teeth = 'white'
hair = 'brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} cm tall.")
print(f"He's {weight} pounds heavy")
print(f"He's also {weight_kg} kg!")
print("Actually that's not heavy")
print(f'''He's  got {eyes} and {hair} hair.
His teeth are usually {teeth} depending on the coffee''')

total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}.")