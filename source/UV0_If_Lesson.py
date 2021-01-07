#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:16:09 2021

@author: yuvi
"""

name = str(input("What is your name?:"))
health = 5
food = 1
hunger = 5

while health > 0 and  hunger > 0:
  action = str(input('What do you want to do:'))
  if action == 'help':
      print("hit, run, explore, build")
  elif action == 'end game':
      print("the game has ended")
  elif action == 'explore':
      print(name + ' explored a cave and found a goblin! the goblin attacked!')
      health = health - 2
      hunger = hunger - 1
      print(health)
  elif action == 'hit':
      print(name + ' hit the goblin and it died, leaving you with it meat as food.')
      food = food + 1
  elif action == 'eat':
      print(name + ' ate some food and made your belly nice and round.')
      health = health + 1
  elif action == 'chop':
      print ('you chopped down some trees and now have some wood')

  if action == 'search':
     print(name + ' you looked around and you found a lake.')
     swim_or_search  = input('Do you want to swim or keep searcing : ')
     if swim_or_search == 'keep searching':
         print('You looked around and a large, fat, wizard')
         talk_or_kill = input('Do you want to talk to or kill the wizard: ')
         if talk_or_kill == 'talk':
             print('You forgot he was a wizard and when you started talking he turned you into a frog. You died.')
             print('Game Over')
             break
         if talk_or_kill == 'kill':
             print('You killed and gained his magic wand you now know all spells')
             wand = input('If you want to access these spells type spells123:')
             if wand == 'spells123':
                 print('You have sucsessfully became a god! Game over...for now')
                 break
     if swim_or_search == 'swim':
        print('You swam and found 3 fish.')
        food = food + 3
  if action == 'build':
         print(' You can build a house, a fire, or a compass')
         build_action = input('what would you like to build?')
         if build_action == 'fire':
             print('the fire is only a spark, you can put oil or blow')
             oil_fire = input('would you like to apply oil or blow on it:')
             if oil_fire == 'blow':
               print('your hard work payed off, and you got a great fire. You found a fish and ate it, and it was cooked weel so you got twice the food')
             if oil_fire == 'oil':
                 print('the flame from the fire was to big, and you started a forest fire, you barly made it out alive')
                 hunger = hunger - 3
         if build_action == 'compass':
             print('you made a compass, but you do not know where to go')
             where_to = input('which way d you want to go?, left, right, forward, backward.')
             if where_to == 'left':
                 print ('you found a town, and got some veggies, you now have 2 more food items')
                 food = food + 2
             if where_to == 'right':
                 print('you wandered off and found nothing')
             if where_to == 'forward':
                 print('you wandered off and found nothing')
             if where_to == 'backward':
                 print('you wandered off found a great bear. you escaped, but lost energy')
                 hunger = hunger - 2
         if build_action == 'house':
             print('you have built a house, but bear destroyed it all. Uh Oh.')