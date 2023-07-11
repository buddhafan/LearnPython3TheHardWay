#Setting a value for a variable named "formatter"
# Use the "format" function to turn the "formatter" variable into other strings
formatter = "{} {} {} {}"
print(formatter. format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your\n",
    "Own text here\n",
    "Maybe a poem\n ", 
    "Or maybe a song about fear"
))