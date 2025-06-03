# WHILE LOOP IN LOOPING STATEMEMENTS, ALSO BREAK, PASS & CONTINUE STATEMENTS:

# WHILE LOOP : 
''' ex :
i = 0
while(i<3):
    print(i)
    i = i +1

'''
# decremented loop:
''' ex :
count = 5
while(count>0):
    print(count)
    count = count - 1


'''

# ELSE IN WHILE LOOP/ FWHILE LOOP WITH ELSE : "python allows the else keyword in a for loop & while loop" the else  specifies a block of code to be executed, when the loop is finished.
#                                 |----> also The else block will NOT be executed if the loop is stopped by a break statement.
''' ex :
n = int(input())
i = 1
while i < n:
    print(i)
    i = i + 1

else :
    print("WHILE LOOP KHUD SE KIA")

''' 

 
# printing 0 to 5 & print a message when the loop is finished : is done using else keyword

''' ex :
k = 0
while(k <6):
    print(k)
    k +=1
else:
    print("else with while loop")



'''
'''  ex :
count = -5
while(count>0):
    print(count)
    count = count - 1
else:
    print('gul')



'''

# The else block will NOT be executed if the loop is stopped by a break statement.
# interview question : break statement lgane ke bd else statement print hogi ki ni ?


''' ex :
n = int(input())
i = 1
while i <n:
    print(i)
    i = i + 1
    if i == 4:
       break

else:
    print("WHILE LOOP KHUD SE KIA")


'''
# Continue and break statement in while loop:
# break statement : 
''' ex :
n = 7
i = 1
while i <n:
    print(i)
    i = i + 1
    if i == 6:
       break

'''
# Continue statement :
''' ex :
i = 0
while i < 6:
  print(i)
  if i == 3:
    continue
  i += 1

'''


# pass statement:
''' ex :
i =  0
while i <6:
  pass
'''
def is_leap(year):
    leap = False
    leap1 = True
    if year %4 ==0:
      return leap1
    elif year%100 !=0 :
        return leap
    elif year% 400 ==0:
        return leap1

year = int(input())
print(is_leap(year))
    