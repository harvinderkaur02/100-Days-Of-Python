#lec 58 : 

#           |---------->

# Decorators in python : wo fn hote h jo ki dusre fn ko  change krke return karte h 
#           |---------->  i simple terms, it's a function which takes anoter function, update it & return it in a new form.
#           |----------> basicaly we just modifying the function


#  how it's work & how does @syntax works in pyton ?
# why should we use decorators?-- hum aisa kyu chahenge, ek fn hai jo ek fnreturn krrra h,   what's motive behind all of this?
#  let's create a simple fn

''' ex :
def hello() :
    print("hello baby") 
hello()  

'''
# now we want to create a fn  we want that first  fn do gm & then do something &

''' ex : detailed explanation of this

def greet(fx) :  
    def mfx():
     print("Good Morning!")  
     fx()
     print("Thanks for using this functions")
    return mfx

# now we will add @greet decorator fn in add fn  : bcoz greet naam ka fn bnaynge jo ki ek fn as a input lega or fn hi return krega--
# basically we just modifying a function, # decorators : just modifying a function.
# how will greet fn modify : it modifying the helllo fn
@greet                     # greet is a decorator that  decorate the hello fn
def hello() :
    print("hello baby") 

def add(a,b):
    print(a+b)
hello()
# decorator : A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
#     |-----> The new function is often referred to as a "decorated" function.   


'''
# normal simple  code of above
''' ex :
def greet(fx) :  
    def mfx():
     print("Good Morning!")  
     fx()
     print("Thanks for using this functions")
    return mfx

@greet                     # greet is a decorator that  decorate the hello fn
def hello() :
    print("hello baby") 

def add(a,b):
    print(a+b)
hello()       

'''


# another way og decorators
''' ex :
def greet(fx) :  
    def mfx():
     print("Good Morning!")  
     fx()
     print("Thanks for using this functions")
    return mfx

#@greet                     # greet is a decorator that  decorate the hello fn
def hello() :
    print("hello baby") 

def add(a,b):
    print(a+b)
greet(hello)()           

 ''' 

# practical use of decorator function 
''' ex :
def greet(fx) :  
    def mfx(*args, **kwargs):
     print("Good Morning!")  
     fx(*args, **kwargs) # fx run with args & kwargs
     print("Thanks for using this functions")
    return mfx

@greet                     # greet is a decorator that  decorate the hello fn
def hello() :
    print("Hello world") 
#@greet
def add(a,b):
    print(a+b)

hello() 
greet(add)(1,2) 



'''
''' ex : another form
def greet(fx) :  
    def mfx(*args, **kwargs):
     print("Good Morning!")  
     fx(*args, **kwargs) # fx run with args & kwargs
     print("Thanks for using this functions")
    return mfx

@greet                     # greet is a decorator that  decorate the hello fn
def hello() :
    print("Hello world") 
@greet
def add(a,b):
    print(a+b)

hello() 
# greet(add)(1,2)   
add(1,2)  



'''
print(10>5 and 5<3)


