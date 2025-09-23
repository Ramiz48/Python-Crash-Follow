print("hello world") 
# Python Basics

#**Data variables:** 

#Boolean =  True or False

#String = “Ramiz” any series of characters

#Integers = numbers

#Float =  1.2, 3.4, 5.7, # Basically numbers in decimals

#None = None (you can write None as a None and it gives no error which means its acceptable not like other string where you have to must put double comma’s.)

#**Type casting** : is basically converting anything into another one like string into int form.

#For Example:

A = “5”

print(A + 1) # in that scenario we have to first convert this into int like (int (5) +1)

B = 5

print (B +1 )

#**Operators:**

#**1: Arithmetic Operators:**

num1 = 10

num2 = 2

print("num1 + num2 is ", num1 + num2) 

print(”num1 - num2 is “, num1 - num2) 

print(”num1 * num2 is “, num1 * num2)

print(”num1 /  num2 is “, num1 / num2)

print(”num1 /  /  num2 is “, num1 /  / num2) # it eliminate numbers after decimal.

print(”num1 ** num2 is “, num1 ** num2) # it gives us power like 10 power 10 it makes 1000

print(”num1 % num2 is “, num1 % num2) # it gives us reminder like 10/1 and reminder will be 1

#**2: Assignment Operators:**

A = 4 # in that case our “=” is assignment operator

A += 2 # in that case it added 2 in above A which is = 4 and the ans will be 6.

A -= 2 # will be 2.. hence it is subtracting that values from above A

A *= 2

A /= 2

print(A)

#**3: Comparison Operator:** What they do is they compare two operators like:

x = 8

y = 3

print(x>y)

print(x<y)

print(x≠y) # is not equal to

print(x==y) #wheather is equal to or not

#4: **Logical Operators:** for making logics

print(x==z **and** x<y)

print(x==z **or** x<y)

print(**not**(False))

print(**not**(True))





#**Packages:**

#In python there are plenty of packages already installed you can use them just after the installation. use them to reduce your efforts, time as well as efficiency.

#like “pip install panda” # type this into the Terminal.. after that it will start installing that particular software.
#Then use it as :
import pandas # "or you can write it this way to for shortcut" import pandas as pd
df = pd.read_excel("file.xlsx") # Basically its function from the pandas libarary to read excel file.
print(df)


#String Operators:
name = "Ramiz" # or we can write it in single quotes to like that 'Ramiz'
print(name)
print(name[0:3]) # in that case it will return the strings on that locations, like Har etc

#String Methods: We can use latest methods by searching on google "string methods python doc" and there
#we can see the methods like: str.find, str.format, etc


#User input: We use this when we need to get user opinion or any answer from them.
name = input("Enter your name: ") # whatever user will write it will be stored in the name variable
print("Hello " + name)

#Lists: Lists are used to store multiple items in a single variable.
#Lists are created using square brackets:   
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0]) # it will return apple
fruits.append("orange") # it will add orange to the list
print(fruits)   
fruits.remove("banana") # it will remove banana from the list
print(fruits)
#List methods: We can use latest methods by searching on google "list methods python doc" and there
#we can see the methods like: list.append, list.remove, etc 

#Tuples: Tuples are used to store multiple items in a single variable.
#Tuples are created using parentheses:
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0]) # it will return apple
#Tuples are immutable which means we cannot change, add or remove items after the tuple is
# created. Hence the below methods will give error if we try to use them.
#fruits.append("orange") # it will give error
#Tuple methods: We can use latest methods by searching on google "tuple methods python doc"
# and there we can see the methods like: tuple.count, tuple.index, etc


#Sets: Sets are used to store multiple items in a single variable.
#Sets are created using curly brackets:
fruits = {"apple", "banana", "cherry"}
print(fruits)
print("apple" in fruits) # it will return True
fruits.add("orange") # it will add orange to the set
print(fruits)
fruits.remove("banana") # it will remove banana from the set
print(fruits)
#Set methods: We can use latest methods by searching on google "set methods python doc" and there
# we can see the methods like: set.add, set.remove, etc


