# CONDITIONALS STATEMENTS IN PYTHON :

# Conditional statments:  are also cld decision making statements.
#                 |-----> based on these conditions  we will execute the next block of code.
#                 |-----> Decision-making statements in programming languages decide the direction of the flow of program execution. 
#                 |-----> also sometime program needs to check the evaluation of certain expressions(s),whether the expression(s) evaluate to True or False
#                 |-----> Based on this, the conditional statements are further classified into following types:
#                                    |
#                                    |-------->  if
#                                    |-------->  if-else
#                                    |-------->  if-else-elif
#                                    |--------> nested if-else-elif.
#                                    |--------> short hand
#                                                 |--------> if
#                                                 |--------> if-else

''' note : identation is important in these statements : python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
           Other programming languages often use curly-brackets for this purpose.'''
# note : also brackets is optional in conditions statements to put conditions


# 1. if statement : also called selection statements
#       syntax: 
#                       if () :
#                        statemets to be executed if is true
            
''' ex 1 : 
 a = 22
b = 30
if (b > a) : 
   print("b is Greater")
 
 '''

''' ex 2:
age = int(input("Enter your age"))
print("Your age is : " , age)
if (age> 18):
    print(" you can vote")

'''

#   2. if- else statements :
#       syntax: 
#                       if () :
#                        # statemets to be executed if is true
#                        else :
#                        # statemets to be executed if , if is false
''' ex :
age = int(input("Enter your age"))
print("Your age is : " , age)
if (age> 18):
    print(" you can vote")
else: 
    print("You cannot vote")

'''
''' ex :
a = 22
b = 30
if (b > a) : 
   print("b is Greater")
else:
   print("a is Greater")

'''
#  3.  if-elif- else statements : also cld elif statements , used to check multiple conditions &
#                                 multiple elif can be applicable

#       syntax: 
#                       if () :
#                        # statemets to be executed if is true
#                        elif :
#                        # statemets to be executed if , if is false
#                        else :
#                        #statemets to be executed if , if is false

''' ex: 
input = int(input("enter the value :  "))
print(" the value is : ", input)

if (input > 0) :
    print("it is positive")
elif (input == 0) :
    print(" it's is zero")
else :
    print("it's is negative")

'''

# 4. Nested-if-elif-else/ Nested-if-elif statments : when we want check conditions inside the conditions

#       syntax: 
#                       if () :
#                        # statemets to be executed if is true

#                        elif() :
#                        # statemets to be executed if , if is false 
#                            if () :
#                             # statemets to be executed if is true
#                            elif :
#                             # statemets to be executed if , if is false
#                            else :
#                             n nn            #statemets to be executed if , if is false

#                        else :
#                        #statemets to be executed if , if is false

''' ex :
value = input("enter your input : ")
print("your input is : ", value)
 
if (value >= 'a' and value <='z' ) :
    print("Input is Lowercase")
elif ( value >= 'A' and value <='Z') :
     print("Input is Uppercase")
elif(value >= '0' and value <='9') :
     print("Input is Numeric")
else :
     print("Input is not valid")



'''
# SHORT HAND - if statement : If you have only one statement to execute, you can put it on the same line as the if statement.
# syntax : if condition: statement
''' ex :
c = 5
d = 10
if d / c : print(" d is divisible by c")

'''

# SHORT HAND if -else statement : If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# syntax :  statement(ehen true) if condition else when condition false
''' ex :
i = 10
print("true") if i > 5 else print("false")

'''
# You can also have multiple else statements on the same line:
''' ex :
One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

'''

# IF YOU WANT TO COMBINE MULTIPLE CONDN  IN A CONDITIONAL STATEMENTS THEN USe LOGICAL OPERATOR (and, or, not)

# by and keyword :
''' ex :
txt = "Yellow"
if txt >= 'A' and txt <= 'Z' :
    print("it's uppercase")

'''
# by or keyword :
''' ex :
txt = "Yellow"
if txt >= 'A' or txt <= 'z' :
    print("it's bothcase")

'''

# by not keyword :
''' ex :
e = 20
f= 30
if not e > f :
    print(" f is greater")
'''
# Pass STATEMENT  : if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
''' 
Example : 
a = 33
b = 200

if b > a:
  pass 
   
'''
# USING time MODULE :  TO give time
# strftime () :  is a function that give the hour(%H), Minute(%M), Second(%S) of a time.

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
x = dir(time) # dir() function is used to get the list of all function, variables in a module
print(x)
# to learn more about time module click on the below link :
# https://docs.python.org/3/library/time.html#time.strftime  


