# LECTURE 5 AND 6 

# lecture = 5 

#  PYTHON ESCAPE SEQUENCE CHARACTER :An escape character is a backslash \ followed by the character you want to insert
# note :  To insert characters that are illegal in a string, use an escape character.

#  1. (\" )  for double quotes
"""" 
example 1 :  inserting a double quotes ()"") inside the string that are already surrounded by double quotes-- that's gives a error
            txt = "I am " Harvinder KAUR" from faridabad "
                            |
                           \ / using (/")
             txt = "I am \" Harvinder Kaur\" from faridabad. "
             print(txt)

"""
#  2. (\n) for a new line
"""" example 2 :  to place the character in a new line use \n
            
             txt1 = "I am \" Harvinder Kaur\" \nfrom faridabad. "
             print(txt1)

"""
# 3. (\b) for backspace
""" example 3. 
                    txt2 = "I am Harvinder \bKaur"
                    print(txt2)

"""
# 4. (\') for single quotes
""" example 3. 
                    txt3 = "I\'m Harvinder Kaur"
                    print(txt3)

"""
# 5. (\t) for tab
""" example 3. 
                    txt4 = "I am Harvinder Kaur \tfrom faridabad"
                    print(txt4
"""
# note : in python, there are so many escape sequence character, learn in string topics

#  MORE ON PRINT STATEMENTS : 

#  1. use of sep= seoerators : in print statement you want to print multiple values can seperate them by using any character

'''  ex
print("GUL", 22, 3, sep = "-") 
'''

# 2. use of end = end(value) : in print statement you want to print something with end value/value with whom u print, then we use end parameter

# print("Hargul" ,end = "26")                        #Ex =1 

"""
print("Hargul", end="26" )                            #Ex= 2 PRINT IN MID- VALUE
print("love")
"""
'''
print("Degre", end="2021\n" )                          #Ex= 3 USING NEW LINE (\n) (escape character)
print("B.Tech-CSE")
'''
# PYTHON COMMENTS : already done in lec 1

# ---------------------------------------------------------------------------------------------------------------------

#LECTURE 6

# VARIABLES :already done in lec 1

# DATA TYPES : specifies the type of value that variable hold.mmm 
#              refers to a type of value u store in memory, also it's show kitna space memory mein lega.
#              Variables can store data of different types & different types can do different things.
#             every variable is associated with a data type.
''' note : Since everything is an object in Python programming, data types are actually classes and variables are 
           instances (objects) of these classes.
'''
# Python has the following data types built-in by default, in these categories=
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# 1. Numeric  data types :  represents the data that has a numeric value.
#                         A numeric value can be integer, floating number, or even complex number. 
#                         These values are defined as int, float, and complex classes in Python. 
#  Integers - This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be.
""" For example:
var1 = 55
print(var1)
print("Type of var1 = ",type(var1))

"""

# Float - This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point.
#  Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
""" For example :
var2 = 78.90
print(var2)
print("Type of var2 = ",type(var2))
"""

#  Complex Numbers - Complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j. 
#                  - is also created like this : ex : 8+2j ---> complex(8,2)
'''  For example :
var3 = 2+3j
print(var3)
print("Type of var3 = ",type(var3))
''' 

#  2. text data type : represents the data that has a text value.
#                      value can be text , characters, string. 
#                     These values are defined as str(string) classes in Python.
#                     this data type also come in sequence data type.
#                  in Python, does not have a character data type, a single character is simply a string with a length of 1.

# string : is a collection of one or more characters put in a single quote, double-quote or triple quote.
#           it's represented as a str class.
#            strings are array 
''' ex 
str1 = 'string with a use of single quotes' 
str2 = "string with a use of double quotes"
str3 = """string with a use of single-triple quotes"""
str4 = """string with a use of double-triple quotes """
print(str1)
print(str2)
print(str3)
print(str4)
print("Type of str1 = ",type(str1))
print("Type of str2 = ",type(str2))
print("Type of str3 = ",type(str3))
print("Type of str4 = ",type(str4))

'''
# note : You can assign a multiline string to a variable by using three quotes (""" """) / (''' ''')
''' for ex : 
str = """hey, Myself Harvinder Kaur
from Faridabad, & pursuing 
B.tech in CSE with specialization in AI & ML
from aravali college of engineering and management,
 """
print(str)
'''  
# Strings are Arrays : In Python, Strings are arrays of bytes representing Unicode characters.
#  
# accessin characters(elements of string) : in Python, individual characters of a String can be accessed by using the 
#                                           method of Indexing.
# Indexing :  allows negative address references to access characters from the back of the String, e.g. -1 refers to the last
#            character, -2 refers to the second last character and so on.
#            in simpler, indexing start with 0 
''' ex :

strr = "Harvinder"
print("acessing first character : ", strr[0])
print("acessing last character : ", strr[-1])

'''

#  3. SEQUENCE data type : is the ordered collection of similar or different data types.
#     Sequences allow to store multiple values in an organized and efficient fashion. 
#     There are several sequence types in Python - list
#                                                - String
#                                                - Tuple
#                                                - range
                                                              
# List : are used to store multiple items in a single variable
#    |--->    is a ordered collection of elements enclosed within [] Square brackets,
#    |--->    are muteable,  is items are ordered, changeable, and allow duplicate values.
#    |--->    list can contain any number of elements and of any datatype (like strings, integers, list, etc.).
#    |--->    List items are indexed: items can be accessed using positive indexing & nedative indexing,
#                                   |
#                                   |--->positive indexing :the first item has index [0], the second item has index [1] etc.
#                                   |--->negative indexing :the last item has index [-1], the second last item has index [-2]
''' ex :
li = ['a', 1, 3.14, True, False]
print(li)

# Accessing elements of list using positive & negatibbe indexing
print(li[0])                           # Accesing first element using positive indexing
print(li[-1])                          # Accesing last element using negative indexing
print(li[-2])                          # Accesing second last element using negative indexing
print(li[1:5])                         # Accesing Mid elements using positive indexing

#  CREATING A EMPTY LIST
li1 = []
print(li1)
print(type(li1))
'''
# TUPLE :     are used to store multiple items in a single variable
#       |---> is a ordered collection of element enclosed within a round brackets/ parenthesis ().
#       |---> are immuteable, is items are ordered, changeable, and allow duplicate values.
#       |---> tuple can contain any number of elements and of any datatype (like strings, integers, list, etc.).
#       |---> tuple items are indexed: items can be accessed using positive indexing & nedative indexing,
#                                   |
#                                   |--->positive indexing :the first item has index [0], the second item has index [1] etc.
#                                   |--->negative indexing :the last item has index [-1], the second last item has index [-2]
''' ex : 
tup1 = (1,'a', True)
print(tup1)

# Accessing elements of tuple using positive & negatibbe indexing
print(tup1[0])                           # Accesing first element using positive indexing
print(tup1[-1])                          # Accesing last element using negative indexing
print(tup1[-2])                          # Accesing second last element using negative indexing
print(tup1[1:5])                         # Accesing Mid elements using positive indexing

#  CREATING A EMPTY tuple
tup2 = ()
print(tup2)
print(type(tup2))

'''

#  4. BOOLEAN TYPE : represent one of two values: True or False
#                    It is denoted by the class bool.
#  Note - True and False with capital 'T' and 'F' are valid booleans, otherwise python will throw an error.
 
''' ex : 1  
bool1 = True
print(bool1)

'''
# When we compare two values, the expression is evaluated and Python returns the Boolean answer:
''' ex : 2
aA = 5
bB= 10
print(aA>bB)
print(bB>aA)
print(aA == bB)
'''
# When you run a condition in an if statement, Python returns True or False:
''' EX : 3 COMPARE TWO NO. 

num1 = 55
num2 = 100
if (num1> num2) :
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")


'''
# Evaluates values & Variables : The bool() function allows you to evaluate any value (of any type), and give you True or False in return,
''' ex : evaluating values :

print(bool("HELLO"))                                # Strings o/p is converted bool o/p
print(bool(0))

 '''                                

''' ex : evaluating variables :
abb = 100
baa ="STRING"
Print(bool(abb))
print(bool(baa))


'''

#  NOte : in boolean data type : almost any value is evaluated to True if it has some sort of content.
#                                 |---->  Any string is True, except empty strings like "" 
#                                 |---->  Any number is True, except 0.
#                                 |---->  Any list, tuple, set, and dictionary are True, except empty ones likes (), [], {}. 
#                                 |---->   & the value none gives false

# Functions can Return a Boolean : You can create functions that returns a Boolean Value:
''' ex : 
def boolfunc() :
    return True

boolfunc()
print(boolfunc())

'''
# Python also has many built-in functions that return a boolean value, like the isinstance() function,
# isinstance() functuon  :  can be used to determine if an object is of a certain data type:
#  syntax : isinstance(variable name, data type)

''' 
Hi = 25                                             # ex 1              
print(isinstance(Hi, int))

JJ = 'PYTHON'                                       # ex 2
print(isinstance(JJ, str))

KK = 22                                             # ex 3
print(isinstance(KK, float))


'''

# 5. Mapping Data type : represent the data which has value like a map
#                        mapping data type is a dict; are used to store data in key-values pairs 

# Dictionary : is a ordered collection of  key-values pairs enclosd in a curly brackets ,
#        |---->  &  Each key-value pair in a Dictionary is separated by a colon :
#        |---->  whereas each key is separated by a ‘comma’.
#        |---->  Values in a dictionary can be of any datatype(no, string, list ) and can be duplicated, but key's can't be same; they are immuteable
#        |---->  Dictionary can also be created by the built-in function dict(). 
#        |---->  An empty dictionary can be created by just placing it to curly braces{}. 
#        |---->  in dict, key can be of any type (integer, mixed(string+ int))
#        
''' ex :1

dict1 = {
    "name" : "GUL",
    "age"  : 21,
   "location" : "India"

}
print(dict1) 
print(type(dict1))  
'''
#  creating a  empty dict
''' ex 2: empty dict

dict2 = {}
print(dict2) 
print(type(dict2))      

'''
# creating a dict using dict() function
''' ex 3 : using dict() function
dict3 = dict({"Company": "Acenture", "Role" : "SDE" , "NOP" : 2 })    
print(dict3)

'''
# creating a dict using dict() function, in which each item as pair (key, value) 
''' ex : 
dict4 = dict([ ('fruit', 'Apple'), ("NO", 2)])    
print(dict4)

'''
# creating a dict with a different type of key :
''' ex :

dict5 = {
    1 : "apple",
    "colors " : 5,
    "list" : [1, 2, 3]
}
print(dict5)

'''
# 6.  Set data type : are used to store multiple items in a single variable.
#                   are of two type : ----> SET
#                                     ----> FROZENSET

#     SET:   A set is a collection which is unordered, unchangeable*, and unindexed(but item can be add or delete using some fn), 
#      |---->  set items are enclosed in a {},  not allowed duplicate items
#      |---->  The values True and 1 are considered the same value in sets, and are treated as duplicates, b/w these 2 values print only First value
#      |---->  The values False and 0 are considered the same value in sets, and are treated as duplicates , b/w these 2 values print only first value
#      |---->  set items can be of any data tyype.
#      |---->  set can be create using set() function, or set constructor()
''' ex :
set1= { "string", True , 1, False, 0}
print(set1)

# create a empty set :
set2 = {}
print(set2)
print(type(set2))
'''
#   Frozenset : Frozen set is just an immutable version of a Python set object. 
#               While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.

# 7. None data type : represent the data which has null/ empty value .it's represented by none keyword
#                     it's come in none class
#                  The None keyword is used for defining a null variable or an object in Python.
#                  None is the same as 0 in Python.
#                  If we compare None to anything, it will always return False in Python, except while comparing it to None itself.
''' ex :
none1 = None
print(none1)
print(type(none1))

 '''
#  8. Range data Type : represent the range of data .
#                 |----> it's represented by range class
#                 |----> its created by range() function 

# range() function : returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
#                    and stops before a specified number.
''' ex :
range1 = range(6)
print(range1)                                   # get range
print(type(range1))    

#  Create a sequence of numbers from 0 to 5, and print each item in the sequence:

x = range(6)
for n in x :
 print(n)

'''

