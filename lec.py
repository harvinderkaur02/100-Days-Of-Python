#DATA STRUCTURE IN PYTHON
 # 1. list : ordered collection of elements enclosed within [], are muteable
""" li = ['a', 1, 3.14, True, False]
    print(li)
"""

 # extracting a list elements : indexing strt from 0
# print(li[0])                                                 #extracting first element
# print(li[-1])                                                #extracting last element
# print(li[1:5])                                               #extracting middle element

#modify a list

# li[0]= "Gul"                                                  #changing the element at 0th index                             
# print(li)


#li.pop()                                                        #poping (deleting) the last element
#print(li)

#li.append("harr")                                                 #append(adding) a new element
#print(li)

# li.reverse()                                                     #reversing a elelment of list
# print(li)

# li.insert(1,"hargul")                                              #inserting a elemnet at specific index
# print(li)

#li1=["apple", "mango", "orange","yellow"]                           #creating a new list
# li1.reverse()                                                       # sorting  a element of new list
# print(li1)


#LIST BASIC OPEREATION
# li1+li1                                                           #concatenating(adding) a new list
# print(li1+li)

# li2=[1,2,3]                                                       #repeating a elemnet
# print(li2*3)

# 2. DICTIONARY: UNORDERES COLLECTIONS OF KEY-VALUES PAIR ELEMENT ENCLOSED WITHIN {}, ARE MUTEABLE.
d1={"apple": 10, "mango": 20, "orange": 30}
# print(d1)
# print(type(d1))

#extracting key and values

# d1.keys()                                             #extracting the keys
# print(d1.keys())

# d1.values()                                             #extracting the values
# print(d1.values())

#MODIFYING A DICTIONARY

# d1["harrr"]="gul"                                     #adding a new element
# print(d1)

# d1["orange"]= 25
# print(d1)                                               #changing the existing element

#DICTIONARY FUNCTIONS
# d2={"harr":"gul", }                                       #new dictinary                         
# d1.update(d2)                                          #update one's dictionary element with another
# print (d1)

# d1.pop("orange")                                         #poping (removing ) a elemnet
# print(d1)

#CONDITINALS STATEMENTS : DECISION - MAKING STATEMENTS
# IF -ELSE STATEMENTS: 
#                        if(condition){
#                           -------                                   statement to be executed
#                           -------
#                                   }
#                        else{
#                         -------                                      statement to be executed
#                         -------
#                             }


a =10
b= 20
if b>a:
    print("b is greater than a")

    #note: if we not giving a indentation(space) in a if else statements its gives error, if we pressing a tab key its gives indentation

# ex : without indentation
# c= 30
# d = 50
# if d>c
# print('d is greater than c')                      # without indentation

#note: if condition is wrong it doesn't print anything for this we use else

if a>b:
    print('a is greater than b')
    

