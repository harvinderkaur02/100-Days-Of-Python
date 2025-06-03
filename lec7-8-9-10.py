#  LECTURE : 7, 8, 9, 10

# lecture 7 : PYTHON TOKENS 
#             0PERATORS AND CALCULATOR USING PYTHON :
# 
#  => PYTHON TOKENS : are smallest meaningful component/unit in a python program.
#                 All statements and instructions in a program are built with tokens. 
#                  The various tokens in python are : 
#                                  1. KEYWORDS
#                                  2. IDENTIFIERS
#                                  3. LITERALS
#                                  4. OPERATORS 
#                                  5. PUNCTUATORS

#  1. KEYWORDS :   are some specials reserve words in python. they can't be directly used in program
#                 They can’t be used as variable names, function names, or any other random purpose.
#                 They are used for their special features.
''' ex : True , False , class, break , continue , None, try, as , def etc. '''

# 2. IDENTIFIERS : Identifiers are the names given to any variable, function, class, list, methods, etc. for their identification. 
#                    Python is a case-sensitive language and it has some rules and regulations to name an identifier 
#      Rules : 
#       |----> identifiers are case sensitve. ''' ex : age  & Age are two different identifiers        
#       |---->Identifier starts with a capital letter (A-Z) , a small letter (a-z) or an underscore( _ ). 
#       |---->Identifiers can’t start with any other character or a digit.
#       |---->Any other special characters or whitespaces are strictly prohibited in an identifier.
#       |---->Except for letters and underscore, digits can also be a part of identifier but can’t be the first character of it.
#       |----> identifiers follow Camel case, pascal case , snake case naming  

# 3. LITERALS/ VALUES : Literals are the fixed values or data items used in a source code. 
#                       Python supports different types of literals such as:
#                               |----> String literals--
#                                                       |----->  Character literals
#                               |----> Numeric literals                           
#                                               |----> Integers literals
#                                               |----> Float literals
#                                               |----> Complex literals
#                               |----> Boolean literals       
#                               |----> Special literals -- like none    
#                               |----> Literals Collections : Literals collections in python includes list, tuple, dictionary, and sets.
#                                           |
#                                           |----> List literals : t is also a list of comma-separated elements or values in round brackets. it's muteable
#                                           |----> Tuple literals :t is also a list of comma-separated elements or values in round brackets. it's unmuteable.
#                                           |----> Set literals : It is the unordered set of key-value pairs
#                                           |----> Dict literals : it is the unordered collection of elements in curly braces ‘{}’.            

# 4. Operators : These are the tokens responsible to perform an operation(work) in an expression.
#                These are some special-symbols to perform  special operation.
#                                         OR
#                The symbol which contain specific meaningg that can use to perform specific operation are cld operators.

#               Also, the variable on which operation is applied cld operands.
#                operators can be unary & binary.

# 5. Punctuators: These are the symbols that used in Python to organize the structures, statements, and expressions.
#                  Some of the Punctuators are: [ ] { } ( ) @  -=  +=  *=  //=  **==  = , etc.

# => PYTHON TYPE-CASTING : when we want to convert one data type into another data type is called typecasting.
#               |----> Python defines type conversion functions to directly convert one data type to another 
#                       which is useful in day-to-day and competitive programming.
#               |----> There are two types of Type Conversion in Python:
#                            |---->   Implicit Type Conversion
#                            |---->   Explicit Type Conversion
 
#  Implicit Type Conversion: In Implicit type conversion, the Python interpreter automatically converts one data type 
#                            to another without any user involvement. 
''' ex : 
type1= 10
type2 = 25.5
type3 = type1 + type2
print(type(type1)) 
print(type(type2)) 
print(type3) 
print(type(type3)) 

'''
#  Explicit Type Conversion: In Explicit type conversion, data type is manually changed by the user as per their requirement.
#                    |---->  With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type.  
#                    |----> in python , there are some built-in -functions to perform casting.
#                              |----> int() type : This function is used to convert any data type to a int type. 
#                              |----> Float() type : This function is used to convert any data type to a float type. 
#                              |----> complex() type : This function is used to convert any data type to a complex type. 
''' ex : 1
a = int (2)
print(a)
b = int(335.67)
print(b)
print(type(b))
 '''

''' ex 2 : 
 
a = float (2)
print(a)
b = float(33)
print(b)
print(type(b))
 
 '''

''' ex : 3
h = str(2)
print(h)
print(type(h))
y = int("3")
print(y)
print(type(y))

'''

# => PYTHON USER INPUT & OUTPUT :

# What is Console in Python? : Console (also called Shell) is basically a command line interpreter that takes input from the user .
#                       |----> it's takes  one command at a time and interprets it. 
#                       |----> it's also cld terminator.
#                       |----> If our program is error free then it runs the command and gives required output otherwise shows the error message
#                       |---->  to execute a command just press the enter key & our command will be interpreted.

#  Python User Input : Python allows for user input, That means we are able to ask the user for input.
#                  |----> to take input from the users use input() functions.
#                  |----> to take input from the users; The method is a bit different in Python 3.6 than Python 2.7.
#                                            |----> Python 3.6 uses the input() method
#                                            |----> Python 2.7 uses the raw_input() method.
''' ex :
user = input()        #take input from the user
print(user)            # print output 

'''
''' ex 2 :

user_name = input("enter username : ")        #take username from the user
print("Username is : ", user_name)            # print username 

'''
# note : we can also typecast the input to any data type, by specifying the typecast function to input() function.
#  ex : typecast the input to integer
''' 
val = int(input("ENTER INPUT : "))
print(val)
'''
#  ex : typecast the input to float
''' 
val1= float(input("ENTER INPUT : "))
print(val1)
'''
 #  ex : typecast the input to str
''' 
val2 = str(input("ENTER INPUT : "))
print(val2)
'''

# => OPERATORS IN PYTHON :
