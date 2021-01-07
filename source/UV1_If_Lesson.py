#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:23:40 2021

@author: yuvi
"""

# Class Presentation 


'Simple "if" statment'




for f in range(5 + 1):
    if f == f:
        print(f)

# In if statements, the "=" sign is "=="


'''    
If statements are like sandwitches!

the top layer of bread, if
the cheese in the middle, elif
and the bottom layer of bread, else

'''

n = 12
fruits = ['mangoes ' "and " 'bannanas']

for x in fruits:
    if n == 12:
        print(fruits)
        n = n + 1
    elif n == 13:
        print(n)
        n = n + 1
    else:
        print(fruits)


# break functions will stop the loop all together 

# with break functions
i = 1

while i < 2:
    if i == 32:
        print(i)
        i = i + 1
        break
    elif i == 12:
        i = i + .5
        print("hello")
    else:
        break


# a great tool is using user input, this allows you to do much, much more...
z = .5

while z < 1:
    food = str(input('do you want to eat?: '))
    if food == 'yes' or ' yes':
        print("you ate your broccolli and now have a full belly, you are done with dinner now " )
        break
    elif food == 'no'or ' no':
        print('your mom got so angry she turned into a monster NOOOOOOOoooo...GAME OVER')
        break
    else:
        print("yes and no are the only options, please try again")
        
#show too_many_ifs.py example
        
    
      
