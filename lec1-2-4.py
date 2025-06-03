# PYHTON SERIES : FROM ZERO TO ADVANCE 

# PROHRAMMING LANGUAGE : is a way to tell computers what to do?--> means computers ko btana chahte h hum, ki ky krna hai--
#                        wo cheez hum programming languages ke through krte h


# INTRODUCTION TO PYTHON :
# => PYTHON: is a popular programming lang, that can be used on a server/backened ,to create applications
#             like web application, games etc. and created by Guido van Rossum 1989 and release in 1991.
#       |---> it's also cld general-purpose language, bcoz its used everywhere.
#       |---> its dynamically typed prog. lang refers to 
# => FEATURES :
#   1. Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).---INDEPENDENT WORK ON ANY PLATFORM
#   2. Python has a simple syntax similar to the English language. & code readibility
#   3. Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
#   4  Python can be treated as OBJECT ORIENTED PROGRAMMING(OOPS) / Procederual way/ functional way 

# => PYTHON CAN BE USED ON :
#                     |---->    server to create web applications.
#                     |---->    alongside software to create workflows.
#                     |---->    to handle big data and perform complex mathematics.
#                     |---->    Python can connect to database systems. It can also read and modify files.

# => PYTHON VERSIONS:  There are two major Python of versions &  Both are quite different i.e.: --->
#                             Python 2 (quite popular)
#                             Python 3 (most recently used +  major version)

# => INSTALLING PYTHON & DIFFERENT TYPES OF IDES:
# 1. first install python depending upon OS-- mac/ window/linux
# 2. then we need IDEs/ Editor: in which write,run our program such as VS-Code, Pycharm etc
#     pycharm gives all tools by which we easily work in python
# 3. One's Another IDEs is ANACONDA;-  its is a distribution that gives everything of python at a time such as libraries; numPy, Matplotlib
#                                      it gives all libraries in one tool-- no need to install alg se
#                                      its also give a IDE i.e. Jupyter Notebook; is a browser-based interpretor thats run on a browser

# Note: Anaconda have 2 version|->Prompt(for engineer/professional)---> Available in  WINDOW ---> it's a based enviroment, first you need to write a prompt/command "jupyter notebook"
#                              |->Navigator(GUI)---> Available in MAC , WINDOW

# PYTHON EXTENSION:
#  Python file extension:    .py    (for example- nameofile.py )
#  jupter file extension:    .ipynb  (for example- nameofile.ipyb )

# => PYTHON COMMENTS: Comments can be used to explain Python code & that make the code more readable
#                  Comments start with a #, and Python will render the rest of the line as a comment
#
#  EX:        #this is a comment

# for multiline comments: Python does not really have a syntax for multiline comments.
#                         To add a multiline comment you could insert a # for each line:
#       Or, not quite as intended, you can use a multiline string(triple quotes) in your code, and place your comment inside it.
#                           (""" """)    or (''' ''')
#         Reason-->  Since Python will ignore string literals that are not assigned to a variable

# => VARIABLES IN PYTHON: are named memory location: basically to access the data in the memory location by its name.
#                   |--->  are containers/temporary storage spaces for storing data values.
#                   |--->  here temporary storage refers to that it value even change type after they have been set.

#  1. for creating a variable: there is no command to declaring a variable, it is created in the moment when we assisgn a value to it.
"""   for exaample 1 : 
                                                     z=5
                                                     y=6
                                                   print(z)   # output is 5

      for example 2 : temporary storage exmple/ dynamially typed language                    
                                                   x=5                          
                                                   x="gul"                                             
                                                   print(x)   # output is gul


"""
#  Note : you can change the value of variable(data type) even after they've been set value
""" 
 a = 5              # a is of type int
# print(a)          # output = 5
#  Now changing its value
a = "HAPPY"         # a is now type of str
print(a)             # output = HAPPY

"""
#  TYPE CASTING : refers to change the data type of any variable into another data type
""" Example: 
               
              b=  str(3)                         # 3 is type cast into str
              c=   int(4)                         # 4 is type cast into int
              d= float(5)                         # 5 is type cast into float
              print(b,c,d)
"""               
#  GET THE TYPE OF ANY VARIABLE: if u want to know get the type of any variable, you can get it by type() function.
""" example:
             
            e = "GUL"
            F =5
            f = 8.879
            print(type(e))                     # print--->  <class str>
            print(type(F))                     # print--->  <class int>
            print(type(f))                     # print--->  <class float>

"""
#  VARIABLES NAMING : 
#            |------> A variable name must start with a letter(a-z or A-Z) or the underscore character
#            |------> A variable name cannot start with a number 
#            |------> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#            |------> Variable names are case-sensitive
"""  example :
                     age = 6
                     Age = 7
                     AGE= 9
     # are three different variables

""" 
#   note :    A variable name cannot be any of the Python keywords.
#   |------>   Cannot include any space or any other character
#   |----->  a variable can've short names (like x & y) or more descripitive names
"""      example : 
                           B = 5
                           myvar = "H"
                           Print(B, myvar)
"""
#                           A variable names can follow camel case, pascal case, snake case naming
""" Example of Multiwords variable name: 

                            myVar = "GULLU"                                     # ex of camel case
                            MyVar ="deepe"                                      # ex of pascal case
                            my_var = "harrr"                                    # ex of snake case 
                            print (myVar)
                            print(MyVar)
                            print(my_var)

"""
# a variable name cannot include any space , any another character or number in starting
"""FOR  example: 
              2myvar = "John"
              my-var = "John"
              my var = "John"
""" 
#  ASSIGN MULTIPLE VALUES IN PYTHON :
# 1.  many values to multiple variables in one line : we can assign a values in multiple variables in one line.
""" example: 
              h, i, j = "PINK", "ORANGE", "YELLOW"
              print(h)
              print(i)
              print(j)

"""

# 2. One values to multiple variables: assign the one(SAME)value to a multiple variables
""" EXAMPLE
                              J = K = L = "beautifull"
                              print(J)
                              print(K)
                              print(L)


"""

# 3. unpacking a tuple : refers to when we have a collection of values in a list, tuple etc, Python allows you to extract
#                        the values into variables. This is called unpacking.
""" EXAMPLE :
              Colors =["Red", "Blue", "Yellow"]
              m , n, o = Colors                 # extracting the values of list into a variables
              print(m)
              print(n)
              print(o)

"""
# Note : When we create a tuple,  & we normally assign values to it. This is called "packing" a tuple

# OUTPUT VARIABLES : in python, print() function is used to output/print the variables
""" ex : 
            k = "GOOD"
            print(k)

""" 
# 1. in the print() function we can take multiple o/p variables 
"""" ex : u = 3
          v= 5 
          print (u ,v)
""" 
#  2. for string : we can use the + operator to concatenate the strings
""" EX : 
            H = "Har" 
            G = "gul"
            print(H+G)
"""
#  3.for numbers : the + operator works as a mathematical operation.
""" ex :
            J = 6
            K = 7
            print(J+K)
            
"""
# note : if we concatenate the string and number they will a error.

# GLOBAL VARIABLES AND LOCAL VARIABLES :
# global variable : variable that are created outside a funcation & that can exceess from anywhere cld global variables
#                   can be used by everywhere, both inside & oustide of fn.
""" EX : 
                F = "DON"
                def myfunc():
                  print("GULLU " + F)

                myfunc()

"""
# local variable : variable that are created inside a funcation & that cannot exceess from anywhere cld local variables
#                   can be used only inside the fn.
""" EX :
            D= "DON"
            def myfunc():
              D = "UU"
              print("GULLU " + D)

            myfunc()
            print("GULLU " + D)
 """

#  GLOBAL KEYWORD : to create a global variable inside a function , we can use a global keyword.
""" EX :
                 
                def myName() :
                  global S
                S = "Kaur"

                myName()
                print("Harvinder " + S)
"""
# ALSO, use the global keyword, if u want  to change a global variable inside a function.
""" ex :
                S= "K"
                def myName() :
                  global S
                S = "Kaur"

                myName()
                print("Harvinder " + S)
"""