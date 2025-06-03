#  LOOPINGS STATEMENTS IN PYTHON,ALSO  BREAK , CONTINUE, PASS STATEMENT IN PYTHON  :
# ELSE IN LOOPIN :

# LOOPS IN PYTHON : Kuch chheeze repeat krni ho ya tb tk krni ho jb tk wo cheeze khtm nahi hojati -- toh iske lie loops ka use krte hai
#            |----> Loops concepts make a python programming mpre powerful.
''' ex : m tb tk bananas khareed skta hu jb tk meri jeb mein paise hai                                                                                                                '''
#            |----> Sometimes a programmer wants to execute a group of statements a certain number of times.
#                   This can be done using loops. Based on this loops are further classified into following main types;
#                                                1.  |----> for loop
#                                                2.  |----> while loop

# For LOOPS : is used for iterating over a sequence of iterable objects in python. (that is either a list, a tuple, a dictionary, a set, or a string).
#       |---->This is less like the for keyword in other programming languages, and works more like an iterator method 
#              as found in other object-orientated programming languages.
#       |---->With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.


# looping through a string
''' ex 1: looping through a string 
name = "gullu"
for i in name :   # i refers to  hr ek charcter/letter in name
    print(i)

'''
''' ex 2 :
names = "harrr"
for x in names :
    print(x, end= ",")

'''
''' ex 3 :
naames = "Love"
for i in naames :
    print(i)
    if(i== "o"):
        print("THIS IS SOMETHING SPECIAL")

'''
# Looping through a list / iterate over a list :
''' ex 1 :
list1 = ['A' , 22, True, "Gullu"]
for i in list1:
    print(i)

'''
''' ex 2:
Colors =["RED", "BLUE", "GREEN", "YELLOW"]
for i in Colors:   #iterate each elements in a list
    print(i)
    for x in i:    #iterate each letters in a element
        print(x)

'''
# range() function : example- "how can we print no till 50/ 20,000" this is done using range function 
#           |------> To loop through a set of code a specified number of times, we can use the range() function,
#           |------> The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#           |------> syntax : range (starting value , ending value)
#                                                        or 
#                             range(ending value)  #starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# note : only print the no from starting value to second last ending value.

''' ex :
for i in range(6):
    print(i)
# Note: that range(6) is not the values of 0 to 6, but the values 0 to 5.

'''
# printing not form zero to , then we add +1 in print statement
'''ex :
for k in range (6):
    print(k +1 )

'''
''' ex '''
# to specify the starting value by adding a parameter: range(4, 9), which means values from 4 to 8 (but not including 9):
''' ex :
for x in range(4, 9):
    print(x)

'''
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 22, 2):
''' EX :
for h in range(2,22,2):
    print(h)

'''

#   THE PASS Statement : for loops cannot be empty, but if you for some reason have a for loop with no content, put the pass statement to avoid getting an error.
''' Ex:

for x in "gullu" :
    pass
    
'''
# BREAK & CONTINUE STATEMENT IN PYTHON :

# break statement : With the break statement we can stop the loop before it has looped through all the items: or at a particular iteration.
#                   to exit the loop at particular iteration 

''' ex :
print("table of 2")
for i in range(1,12):
    print("2 X ", i ,"=",2*i)
    if (i == 10):
        break

'''
''' ex :
print("table of 3")
for i in range(12):
    if (i == 10):
        break
    print("3 X ", i+1 ,"=",3*(i+1))
'''
''' ex :
str1 = "HARRr"
for i in str1: 
    if (i =="r"):
        break
    print(i)
 
'''
# Continue statement : With the continue statement we can stop the current iteration of the loop, and continue with the next iteration.
#                      to skip a particular iteration then use continue statement.
''' ex :
for i in range(6):
    if(i== 0):              
        continue             #skip the 0 iteration
    print(i)

'''

# ELSE IN FOR LOOP/ FOR LOOP WITH ELSE : "python allows the else keyword in a for loop & while loop" the else  specifies a block of code to be executed, when the loop is finished.
#                                 |----> also The else block will NOT be executed if the loop is stopped by a break statement.
''' 
INTERVIEW QUESTION : KYA HUM ELSE KO SIRF IF/ FOR LOOP/ WHILE LOOP KE STH HI USE KR SKTE HAI 
    INTERVIEW ANSWER   :    YES

'''
# printing 0 to 5 & print a message when the loop is finished : is done using else keyword
''' ex :

for i in range(1,5):
    print(i)
else :
    print("KHATAM HUAA UFF THAK GYII! ")
'''

# The else block will NOT be executed if the loop is stopped by a break statement.
''' EX :
for k in range(5):
    if k == 3 :
        break
    print(k)
else:
    print("hello")


'''


# NESTED FOR LOOP :
li = ["RED", "BLUE","GREEN"]
li1 =['R','B','G']
for i in li:
    for j in li1:
        print(i,j)
    


n = int(input())
i = 1
while i < n:
    print(i)
    i = i + 1

else :
    print("WHILE LOOP KHUD SE KIA")

