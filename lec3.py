# MODULES AND PIP IN PYTHON
#  MODULES : are used to borrow someone's else code in your program: which means: you can use someone else code in your program,
#            with the help of these modules

# TYPES OF MODULES: are of 2 type:
#                                  1. Built-in-modules : are the modules that are ship along with python program,-- means jo already python prog. m hote h
#                                                        whiche means there's no need to install them externally; ex : ghr m chheez alreadyjo padi hoti h
# 
#                                  2. external modules: are the modules / is a code wriiten by people & they want
#                                                      you to use their code in your program-- Which can install using pip ; ex: koi cheezz bhr se jo chahiye hoti h ghr m usse krne ke lie
#              example: phone--->use--->application---> we don't know how its work behind---> but we are able to use it .
 
# Note : code wriiten in modules - is a well tested, written by experts & they've very less chances of error--> bcox may people use it
 
#  why we use module : we use modules, bcoz we don't want to code basic program from scratch

# ADvantage of using  modules ; time bachega, efforts bchnge , easily work kr pynge

# PIP: is a package manager what we need in our program/ interpretor  it takes from internet & install in our interpretor.
#  example = hum (khud) ; koi cheez chahiye hoti h lele jate h
#  --> to see pip, write pip in terminal : pip
#  ---> This is write in a terminal -> ex: pip install pandas
# 
# examples of both types of modules:
import pandas           # pip install pandas ------ it's a data- analysis library, ex of external modules
import sklearn          # pip install scikit ------ it's a ML library, ex of external modules
import hashlib          # ex of built-in- modules                                      

# import tenserflow     --> pip install tenserflow ------ it's a ML library, ex of external modules

# -------------------------------------------------------------------------------------------------------------------------

# Module:   Consider a module to be the same as a code library.
#           A file containing a set of functions you want to include in your application.

#  => CREATE A MODULE: To create a module just save the code you want in a file with the file extension .py
"""            EXAMPLE:   in ex3.py--- creating a module with greeting function
                                                                                                          
                                     def greeting(name): 
                                      print("Hello, " + name)      
 """ 

# USE A MODULE: we can use the module we just created by using import keyword
#  example:              import ex3                                         
#                        lec3.greeting("Gul")                          # access the function from a module with a parameter

# => TO EXCESS THE FUNCTION/VARIABLES IN A MODULE :
"""                     use the syntax: module_name.function_name.          # To access the function
                        use the syntax: module_name.variabl_name.          # To access the variable

                        example available  in above & below
"""
# => VARIABLES IN MODULES: 
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
"""
Example
          creating a dictionary which contain some key values pair & Save this code in the file ex3.py

                            person1 = {
                            "name": "John",
                            "age": 36,
                            "country": "Norway"
                            }

"""
"""
example : to acccess the person1 dictionary from ex3 module

                                                 import ex3
                                                 a = ex3.dict2["age"]
                                                print(a)
                                                      
"""

# NAMING A MODULE:     You can name the module file whatever you like, but it must have the file extension .py


# RE-NAMING A MODULE: we can re-create the module named , when we import a module , using as keyword
"""
                                    import ex3 as ex
                                a = ex.dict2["age"]
                                print(a)
"""
 
# BUILT-IN-MODULES :  There are several built-in modules in Python, which you can import whenever you like.
import platform
x= platform.system()
print(x)

# USING THE dir() Function : it's a built-in-function to list/get all the variable /function name in a module
#                            the dir() function can be use on all modules , also te one's you create yourself
#  Exaample: 
""" Exaample: 
                           import platform
                           y = dir(platform)
                           print(y)

"""

# IMPORTS FROM MODULES : We can choose to import the only parts from a module which we want, by using the from keyword
"""  Example
                    The module named ex3 has one function and one dictionary:

                    def greeting(name):
                    print("Hello, " + name)

                    person1 = {
                    "name": "John",
                    "age": 36,
                    "country": "Norway"
                    }
"""
#                                    now
# Import only the person1 dictionary from the module:
from ex3 import dict2
print (dict2["age"])
print(dict2["name"])
print(dict2["country"])

# Import only the greeting function from the module:

from ex3 import greeting
print(greeting("gul"))

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
#  Example: person1["age"],                 \/
# not mymodule.person1["age"]               X

# ----------------------------------------------------------------------------------------------------------------------

#  => PYTHON  PACKAGES : are just like a folder which contain all related python files (modules)
#                        Example: orgainize our files in a different folder/subfolder based on some criteria,so that they can
#                                 be managed efficiently--- similar like packages
#  it's nearly similar to modules-- install/uninstall/using packages is same

# LIST PACKAGES: using the list command to see all the list of all modules/packages installed in our system
#               example: pip list

