#create a bunch of variables with complex strings so that you can see they are for

#string: a bit of text you want to display to someone or"export" out of the program you are writing. Python knows you want something to be a string with either double or single quotes
#can contain any number of variables
#variables are anything with a name = to a value

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # string inside a string

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so funny?? {}"

print(joke_evaluation.format(hilarious))
#make two variables
w = "This is the left side of..."
e = "a string with a right side."
#combine two strings
print(w+e)