# INTRODUCTION TO OOP (OBJECT ORIENTED PROGRAMMING LANGUAGE) :
''' IN PROGRAMMING LANGUAGE  WE'VE A TWO WAY TO WRITE A PROGRAM /CODE :
                                        1. PROCEDURAL WAY : TILL NOW WE DO THIS, CREATING FUNCTION, LOGICS --BASED ON METHODS GIVEN IN PROG                                        2. OOPS: 
                                        2. OOPS:  WHEN WE WANT TO USE/ REAL WORLD ENTITIES (OBJECTS) IN OUR PROGRAMMING WORLD, SO OOPS COMES
                                                                      OR 
                                                  WHE WE WANT TO WORK WITH /OR  (REPRESENT )REAL WORLD ENTITIES (OBJECTS) IN OUR PROGRAMMING WORLD-- >WE USE OOPS

                                        
'''
# TWO IMPORTANTS CONCEPTS IN OOPS :  
#                         |------->  1. CLASS : is blueprint/template for a real world entities/ creating objects
#                         |------->  2. OBJECT : is a specific instance of class

# CLASS : is blueprint/template for a real world entities/ creating objects
#   |---> It defines the properties and methods that an object of that class will have. 
#                      |--->  Properties : are the data or state of an object, 
#                      |---> & methods : are the actions or behaviors that an object can perform.
''' FOR EX : 1                                 
                            PHONE CLASS |---> PROPERTIES (attributes /state/data) : COLOR, COSTS, BATTERY LIFE,
                                        |---> METHODS/BEHAVIOUR (action) : MAKE CALLS, WATCH VIDEOS, PLAY GAMES,
                                        |--->  OBJECTS (TYPES): APPLE, ANDROID , SAMSUNG, MOTOROLA
                                        '''
#   |---> is a collection of objects
#   |---> is a user defined data types
# Attributes are the variables that belong to a class.
#  Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute


# OBJECTS : are specific  instances of class
#   |---> it contains its own data and methods. 
#   |---> 
#   |---> 
''' FOR EX : 1                                 
                            Dog CLASS |---> PROPERTIES : COLOR, Breed, Age,
                                        |---> METHODS/BEHAVIOUR : Bark, EAT, SLEEP,
                                        |--->  OBJECTS (TYPES): STREET, HAVANSE, GERMAN SHEPHARD
 FOR EX : 2                                 
                            PERSON CLASS |---> PROPERTIES : NAME AGE, OCCUPATION ADDRESS,
                                         |---> METHODS/BEHAVIOUR : WALK , SPEAK, MOVE , WORK,
                                         |--->  OBJECTS (TYPES): GUL, HARRR, SIMI, CHOTU, 
'''
#  note: every real world entities we see is a object-- to represent these entites in programming - that's why we required oops

# -----------------------------------------------------------------------------------------------------------------------
# LEC 57 :

# HOW TO CREATE A CLASS : WE CREATE USING CLASS KEYWORD
#                    |--->  class name always starts   with capital letter.
#                         

''' EX 1 :
class Dog :               #creating class
    Dname = "MITHU"       #defining properites
    Dbreed= "STREET DOG"

a = Dog()
print(f" {a.Dname} is a {a.Dbreed}")



'''


''' EX 2 :


'''

''' EX : 3



'''
''' ex 4

class Person :
    name = "gul"
    occupation = "Software developer"
    networth = 0
    # creatin a method
    def info (self):
       print(f"{self.name} is a {self.occupation}")


a = Person()  # creating a person /OBJECT
B = Person()  # creating a another object
c = Person()
B.name = "Harvinder"
B.occupation = "developer"
# a.name = 'HARR'  # A NAME IS CHANGE  THATS IS HARRR
print(a.name, a.occupation, a.networth)
a.info()
B.info()
c.info() # c take a default values.


'''
# class Person :
#     name = "gul"
#     occupation = "Software developer"
#     networth = 0
#     # creatin a method
#     def info (self):
#        print(f"{self.name} is a {self.occupation}")


# a = Person()  # creating a person /OBJECT
# B = Person()  # creating a another object
# c = Person()
# B.name = "Harvinder"
# B.occupation = "developer"
# # a.name = 'HARR'  # A NAME IS CHANGE  THATS IS HARRR
# print(a.name, a.occupation, a.networth)
# a.info()
# B.info()
# c.info() # c take a default values.

# CLASS : A class is a blueprint or a template for creating objects   
#  |----> providing|---> initial values for state (member/ variables or attributes), 
#                  |---> and implementations of behavior (member functions or methods).
#  |----> The user-defined objects are created using the class keyword.

#  HOW TO CREATE A OBJECT :  Object is the instance of the class used to access the properties of the class 

# Self keyword :  The self parameter is a reference to the current instance of the class, 
#              |--->and is used to access variables that belongs to the class.
#              |---> WO OBJECT JISKE LIE / PR  YEAH METHOD CALL KRA JARA HAI
# jb onject create krte h to uss objects se yeh sb methods call krte hai
# inbulit parameters invoke (call) krna ho objects ke sth we use self
''' EX :
or jo bhi method hum class ke andr create krnge phla parameter self rhayega


'''
'''' 
class Phone :
    # defining methods/ behaviours of the class
    def make_calls(self): 
        print("making a phone call")
    #  defining another method/ behaviour
    def play_game(self):
        print(" playing game")
p1 =  Phone()  # CREATING A INSTANCE / OBJECT
p1.make_calls() #ONJECT AB PHONE KR SKTA H  OR GAME KHEL SKTA H  
p1.play_game()



'''
# ------------------------------------------------------------------------------------------------------------------------
# lec 58 : Constructor 

# Constructor : helps to make an object
# sometimes we want to create objects by passing arguments--> at that time , the constructor helps us to intialized in
# previous lec. we see classed & object

''' ex "
class Person :
    name = "Simi"                      #DEFAULT VALUES / #creating (defining) properities
    occ = "Lab Technicinan" 

    def info (self):                  #creating (defining) method
        print(f" {self.name} is a { self.occ}")

a = Person()             #creating object
print(a.name)             #accessing object using dot operator in print function
a.info()                  #invoking method
'''


''' ex 2

class Person :
    name = "Simi"                      #DEFAULT VALUES
    occ = "Lab Technicinan" 

    def info (self):
        print(f" {self.name} is a { self.occ}")

a = Person()
a.name = "Harr"                   #  a name is changed  "simi to harrr"           , also default values   
a.occ = "Developer"               #  a occ is changed  "lab tech. to developer/''
a.info()

 '''
# instead of writing this default value,we need  a way from which i can pass this default value to the class in clear way 
#  that's why constructor is come

# for creating a constructor : special method/keyword/fucntion / is used, called __init() dunder method--> self arg is also used in this
# init method is used to create objects


''' EX : of default constructor : 

class Person :
    # name = "Simi"                      #DEFAULT VALUES
    # occ = "Lab Technicinan" 

    def __init__(self):
        print("Hey i am a person")
    def info (self):
        print(f" {self.name} is a { self.occ}")

a = Person()         #  FIRST object created
b = Person()         # SECOND OBJECT CREATED
'''

#   note : constructor is called (INVOKED ) whenever (jab bhi) we  making an object or jitni br bhi bhi every time jb bhi hum object create krnge outside of the class
#  WHILE TAKING ADVANTAGE OF THIS 
''' ex : (parameterized constructor )

class Person :
    # name = "Simi"                      #DEFAULT VALUES
    # occ = "Lab Technicinan" 

    def __init__(self, n , o):
        print("Hey i am a person")
        self.name = n
        self.occ = o
    def info (self):
        print(f" {self.name} is a { self.occ}")

a = Person("harr", "Developer")         #  FIRST object created
b = Person("gul", " sde")         # SECOND OBJECT CREATED

a.info()
b.info()

'''

# self  object ki form m pass hota h wo bhi automatically  pass hota h
#n , or o yeh object default values di h uski form m pass hue h


# also note self.name or self.occ property h object ki & n or o ek simple sa temporary variable ek argument ki trah passed kia h
#it's just liked a local variable for init() function ke lie 
class Person :
    # name = "Simi"                      #DEFAULT VALUES
    # occ = "Lab Technicinan" 

    def __init__(self, n , o):
        print("Hey i am a person")
        self.name = n
        self.occ = o
    def info (self):
        print(f" {self.name} is a { self.occ}")

a = Person("harr", "Developer")         #  FIRST object created
b = Person("gul", " sde")         # SECOND OBJECT CREATED
c = Person(1,2)
a.info()
b.info()
c.info()

# constructor : A constructor is a special method in a class used to create and initialize an object of a class.
#      |----->  There are different types of constructor.
#      |-----> Constructor is invoked automatically when an object of a class is created.
#      |----->A constructor is a unique function that gets called automatically when an object is created of a class. 
#      |----->  It cannot return any value other than None.
#      |----->The main purpose of a constructor is to initialize or assign values to the data members of that class.
''' Syntax of Python Constructor
def __init__(self):
	# initializations
init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.
'''


#     type of constructor : 
#                        |-----> Parameterized Constructor
#                        |-----> Default Constructor


#  Parameterized Constructor : When the constructor accepts arguments along with self, it is known as parameterized constructor.
#                    |----->  These arguments can be used inside the class to assign the values to the data members.
#                    |-----> The parameterized constructor takes its first argument as a reference to the instance 
#                             being constructed known as self and the rest of the arguments are provided by the programmer.

#  Default Constructor : When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.  
#      |----->
#      |----->
