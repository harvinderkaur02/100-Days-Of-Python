# FUNCTIONS IN PYTHON : A function is a block of code which only runs when it is called.  OR 
#                 |---->  Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task.
#                 |---->  Functions can be both built-in or user-defined.

#                 |----> You can pass data, known as parameters, into a function.
#                 |----> A function can return data as a result.

# WHY USE : The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for 
#             different inputs, we can do the function calls to reuse code contained in it over and over again. 

# creatng a function  : In Python, a function is defined using the def keyword:
''' EX :

def func():
    print("hello from gul")


'''
# CALL A FUNCTION : To call a function, use the function name followed by parenthesis:

''' EX: 1
def func():
    print("hello from gul")

func()

'''
# Arguments : Information can be passed into functions as arguments.
#        |---> Arguments are the values passed inside the parenthesis of the function.
#        |--->  A function can have any number of arguments separated by a comma.
#        |---> Arguments are often shortened to args in Python documentations.

''' EX :2
def CalculateGmean(a, b):
  mean = a*b/a+b
  print(mean)

CalculateGmean(2,3)
c = 3
d =4
CalculateGmean(c,d)

'''

''' ex :3
def CalculateGmean(a, b):
    mean = a*b/a+b
    print(mean)
a = 3
b = 2


CalculateGmean(a,b)

'''
''' ex : 4

def isGreater (a, b):
   
    if (a > b) :
        print("first is greater")
    else :
        print("Second is greater")


isGreater(4, 6)

'''
''' ex : 5 isLesser funcn

def isLesser (a, b):
   
    if (a < b) :
        print("first is lesser")
    else :
        print("Second is lesser")


isLesser(4, 6)

 '''
# pass statement : function definitions cannot be empty, but if you for some reason have a function definition with
#                   no content, put in the pass statement to avoid getting an error.
''' ex :
def gull():
    pass
'''

# no of arguments : You can add as many arguments as you want, just separate them with a comma.
''' ex :
def my_name(fname, lname):
    print(fname, lname)

my_name("harrr", "gull")    
'''

# TYPE OF ARGUMENTS: Python supports various types of arguments that can be passed at the time of the function call.
# arbitary arguments
''' ex
def func(*value):
    print("the value is : ", value[2])

func(1,2 ,3 ,4 ,5)  

'''
# default argument/parameter
''' ex:
def avg(a = 9, b =1):
    print("the avg is : ", (a+b)/2)

avg()   
avg(3,3)
avg(a=2,b = 4)
avg(1)
avg(b = 9)
      

'''
# another ex 
''' 
def name(fname, mname= "Singh", lname= "Rajput"):
    print("Hello,",fname, mname, lname)

name("Harvinder")

'''
# keyword agrumnets
''' ex :
def diff( a , b):
    print("the diff is :", a-b)
diff(a = 6, b= 3)
diff(b= 10, a = 5)

'''

# required argument:
''' ex :
def prod(a, b):
    print('prod is', a*b)

prod(2,3)    
prod(a = 2, b = 5)

'''
# variable length argmument/ arbitary arg (*)
''' ex :
def avg(*num):
    sum = 0
    for i in num:
        sum +=1
    print(" the avg is :", sum/len(num))  
avg(1, 2, 3,4)  
'''
     

# arbitary keyword argument 
''' ex :
def name(**name):
         print("Hello,",name["fname"], name["lname"])
name(fname="Gullu", lname="Don", mname = "hu")

'''
 #   return value:
''' ex :
 def f(x):
    return 5 *x
print(f(
 '''

# 
# lambda function :
''' ex :
x = lambda a: a+10
print(x(5))
'''
''' ex :
x = lambda a,b,c: a+b+c
print(x(5,5,2))


'''
''' ex :


'''
''' ex :
#def double(x):
 #   return x*2
double = lambda x : x*2
print(double(5))

'''
''' ex :
cube = lambda x : x*x*2
print(cube(5))

'''
