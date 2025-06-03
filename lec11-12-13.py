#  STRINGS IN PYTHON :

# => STRING :  is a collection of one or more characters put in a single quote, double-quote or triple quote.
#        |---> it's represented as a str class.
#        |---> it's come in text data type.
#        |---> in Python, does not have a character data type, a single character is simply a string with a length of 1.
#        |---> you can print the string directly with print function or assign a string as a variable  
''' ex : 

str0 = 'Gul'                # string usingg single quotes
str1 = "hello"              # string using double quotes
str2 = """helloooooooo"""  # string using triple quotes
print(str0)
print(str1)
print(str2)
'''
# for  multiline strings :  you can use single-triple quotes / double-triple quotes.
'''ex : using single tripke quotes

str3 = """ Hello i am harvinder kaur,
from faridabad, pursuing B.Tech in CSE(AI&ML), 
From ACEM.
"""   
print(str3)    
'''    
#                           or 
""" ex : using double triple quotes

 str3 = ''' Hello i am harvinder kaur,
from faridabad, pursuing B.Tech in CSE(AI&ML), 
From ACEM.
'''   
print(str3)   

"""
# quotes inside the string/ quotes : You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
'''  ex :
str4= 'I AM "Harvinder KAUR", from faridabad. '
print(str4)

str5= " i'm gul"
print(str5)
'''

# STRINGS ARE ARRAY: In Python, Strings are arrays of bytes representing Unicode characters.
#             |--->  Python does not have a character data type, a single character is simply a string with a length of 1. 
#             |---> Square brackets[],can be used to access elements of the string.

# ACCESSING CHARACTERS IN PYTHON STRING :In Python, individual characters of a String can be accessed by using the
#                                         method of Indexing.

''' INDEXING : In Python, indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number.
           |---> Generally, Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on.
           |---> two types ---> 1. Positive indexing : to access the element from the starting of the string; ex in above. 
           |                |--> 2. Negative indexing :negative address references to access characters from the back of
           |                                           the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 
           |--->While accessing an index out of the range will cause an IndexError.
           |---> Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.
           |---> Space also include in this indexing.       
'''
#    EX :       
# Negative indexing :                         -8  -7  -6  -5  -4  -3  -2  -1                             
#                                            | G | U | L | L | U | D | O | N |
# Positive indexing :                          0   1   2   3   4   5   6   7  

''' Ex :

str6 = "GULLUDON"
print(str6[0])                                                #accessing the first element using positive indexing
print(str6[1])                                                #accessing the second element using positive indexing
print(str6[-1])                                                #accessing the last element using negative indexing
print(str6[-2])                                                #accessing the  second last element using negative indexing
'''

# STRING LENGT :  get the length of a string, use the len() function.
#                 it's also include space & characters.
''' ex : 
a = "STRING"
print(a)
print(len(a))

b = "GULLU DON"
print(len(b))
'''

# STRING SLICING :  to access the groups/collections/RANGE of elements/characters in string by using the slicing syntax (colon :)  sign in the square brackets & along with index value followed the starting & last index value .you want
#            |--->  in this method only: refer starting value & but not last      '''
''' ex :

str6 = "GULLUDON"
print(str6[1 :5])        #inclduing 1 but not 5        #accessing the mid element from index 1 to 5 using positive indexing
print(str6[3 :8])        #inclduing 1 but not 5        #accessing the mid element from index 1 to 5 using positive indexing.
print(str6[:5])        #inclduing 1 but not 5        #accessing the mid element from index 1 to 5 using positive indexing
print(str6[0 : -3])        #inclduing 1 but not 5        #accessing the mid element from index 1 to 5 using positive indexing
print(str6[-3 : -1])        #inclduing 1 but not 5        #accessing the mid element from index 1 to 5 using positive indexing
print(str6[:])         #accessing  all the element from index 0 to 7 using positive indexing
print(str6[-8 :0])        #inclduing -8 but not 0       #accessing all  the element from index -8 to 0 using bothindexing
print(str6[-2 :-7])        #inclduing -8 but not 0       #accessing all  the element from index -8 to 0 using bothindexing
print(str6[-7:len(str6)-3])                                   

'''
# Note: print(str6[-7:-3]) means 
#       print(str6[len(str6)-7 : len(str6)-3])
#       print(str5[1:5])                                       #only for negative slicing
''' ex :
str6 = "GULLUDON"
print(str6[-7:len(str6)-3])
'''
# Reversing a string : we can reverse the string by using [::-1]
#                     We can also reverse a string by using built-in join and reversed function.
''' ex :
str7= "HELLO DON"
print(str7[::-1])
# reversing string by using join & reverse function
str8 = "GULLU"
str8 = "".join(reversed(str8))
print(str8)

'''
# looping through a string : loop  through the characters ,we can excess the string characters by using for loop
''' ex :
for x in "HELLO":
 print(x)
''' 
# CHECK STRING :  
# 1.  to check if certain characeters or phrase  is present in string, we can use the in keyword
"""ex :
st = "python is object -oriented language"
print("object" in st)

t = "i am good"
if "y" in t:
    print("yes, 'am' is present in t")
else:
    print("No, 'am' is not present")
    
"""
# 2. to check if certain characeters or phrase  is not present in string, we can use the not in keyword
"""ex :

str88 = "dim dim dim"
print("y"  not in str88)

string7 = "i feeling blessed"
if "t" not in string7:
    print("NO, 't' is not present in string7")
else:
    print("yes, 't' is  present in string7")

"""

# => MODIFY A STRING : python has a set of built-in methods/functions that we can use on a string.

# following are the string  basic functions(built-in-methods) 
#     |---> Converting string to lower case : use lower() function / method
#     |---> Converting string to upper case : use upper() function / method
#     |---> find length of string           : use len() function / method
#     |---> replace a substring/string: use replace() function / method
#     |---> no.of occurance of string : use count() function / method
#     |---> find the index of substring : use find() function / method
#     |---> remove whitespace in a string  : use strip() function / method to remove space from beginningg or at the end.
#     |---> spliting a string : use split() function / method-> from their specific character,convert the string into substring in list item form
#

""" example of all the above functions :

string1 = "Hello Gullu"  
print(string1.lower())
print(string1.upper())               
print(len(string1))               
print(string1.replace("G","P"))     
print(string1.count("l"))  
print(string1.find("Gullu"))          
    
string2 = " MEIN HU, DON "
print(string2.strip())
print(string2.split(','))

"""
# note : to find length len() function directly with variable use 2underscore before & after in len text, like __len__
""" ex : 
string1 = "Hello Gullu"  
print(string1.__len__())
""" 

# =>  STRING CONCATENATION : To concatenate, or combine, two strings you can use the + operator.
''' EX :
a = "Hello"
b = "World"
c = a + b
print(c)
'''
# To add a space b/w them add " " / or give space in string 
''' ex "
h = "Hello"
g = "gullu"
i= h + " " + g                      # add " "
print(i)

e = "Harrr "             #give space in string
f = "Gul"
j = e+f
print(j)

'''

# => STRING FORMAT/FORMAT STRING :  also clled string interpolation 
''' as we know  we can't string & number by + operator.  '''
#                         |---->    but there's a method to concatenate the string & the no. by using
#                                         |----> 1.  f-string
#                                         |----> 2.  format () method

#   1. f-string : is one such way in python which allow you to place variable(number) very convenient in string.
#       |----> this method -String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#       |---->  To specify a string as an f-string; simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
''' ex 1 :
name = "Gul"
country = "India"
txt = f"MY name is {name} and i am from {country}"
print(txt)
'''
''' ex 2 :

price = 60
txt1 = f"the price is {price} ruppess "
print(txt1)
'''
# placeholders and modifiers in f-string :

# placeholder : A placeholder can contain variables, operations, functions, and modifiers to format the value.
#    |---->  A placeholder can include a modifier to format the value.
''' ex : 
#add placeholder for variable 
age = 22
txt1 = f"My Age is {age} "
print(txt1)

'''
''' ex :
# add placeholder for operator :
txt2 = f"the addition is 2 & 3 is {2+3}"
print(txt2)
print(type(txt2))
'''
# Modifiers : A modifier is included by adding a colon : followed by a legal formatting type, like .2f , .3f 
#             which means fixed point number with 2 decimals, 3 decimals & so on :
''' ex :
price1 = 60
txt3 = f"the price is {price1:.2f} ruppess "
txt4 = f"the price is {price1:.3f} ruppess "
print(txt3)
print(txt4)

'''

#  2. Format() method : this method is used before the f-string to concatenate the string & the numbers  
''' ex 1:

txtt = "MY name is {} and i am from {}"
name = "Harrr"
country = "India"
print(txtt.format(name, country))

# if we reverse format
print(txtt.format(country, name))                # its print reverse



'''
# for the above we used numbers in placeholders
''' ex :
txtt = "My name is {1} and i am from {0}"
name = "Harrr"
country = "India"
print(txtt.format(country, name))

'''
# combine the string & the number
''' ex 2 :

age = 21
txxtt = "my age is {}"
print(txxtt.format(age))

'''

# Disadvantage of format() method : does not give convenience --> writing a lot of code
#                                                            |-->placing a no in placeholder give confussion
#                                                            |--> that's why f-string introduced.

# => PYTHON ESCAPE SEQUENCE CHARACTER :An escape character is a backslash \ followed by the character you want to insert
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
""" example 4. 
                    txt3 = "I\'m Harvinder Kaur"
                    print(txt3)

"""
# 5. (\t) for tab
""" example 5. 
                    txt4 = "I am Harvinder Kaur \tfrom faridabad"
                    print(txt4
"""
# 6. (\\) for backslash 
''' ex 6.
txt7 = "I am Gul//Harr"
print(txt7)

'''
#  others escape characters are :
#   7.  |---> (\f) for form feed
#   8.  |---> (\ooo) for octal
#   9.  |---> (\xhh) for Hex
#   10. |---> (\r) for carriae=ge return

# N-O-T-E : In python there are so many (built-in ) string Methods/ functions that were used in string.

# DOC-STRINGS IN PYTHON : simply help us to understand a function/class/method/ module properly
#                   |---> are string literal that appeat write after the definition of a function, method, class, or module.
#                   |---> are also called documentation string( or doc string)
#                   |---> they are used to document what the object does , encclosed in tripple quotes (single/double)
#                   |---> suppose if we wrote a function & you got the function with description, so it canbe better than this
""" ex :

def square(n) : 
    ''' take in a number n, return the square of n'''
    print(n**2)
square(5)
print(square.__docstring__)

"""
#  note : The doc string are not ignored like comment , to put a docstring -- just above the body of the fucntion or below the name of function
#          it's a special type of string in a python to give a special treatement to this

# comments vs docstring 
#  comments : are description that help program better intend & functionalities of the program
#        |--> are strt with # or ''' ''' / """ """
#        |--> & the python interpretator completly ignore them

# docstring : are string , are short documemtation they provide a description of the function & other methods
#        |--> are start with tripple quotes 
#        |-->they are not ignored by interpretator
#        |-->& can be accessed at run time usingg (functionname.__doc__ ) attribute
#        |--> can be one line or  multiline
#        |--> appear right after the definition of function /class / & other methods
#        |--> are used to code the document


#  Pep-8 : provide a guideline & best practice on how to write a  python code
#     |--> written in 2001 by  Guido Van Rossum,Barry Warsaw, Nick/Alyssa Coghlan
#     |--> its focus is to make a python code consistent readable & maintainable
#     |--> stands for python Enhancement proposal 
#     |--> is a coding style guide proposal for python programming
#     |--> there are so many pep document -- which will tell you how to write  goood , maintainble & great python code


# pep is a  design document  that coding style guide information  OR describiing new feature for its python OR ITS process or environment.

#  Zen of python : is a poem, when we write the "import this " in a shell command --- its give poem of tim peter
''' ex :
import this

'''




