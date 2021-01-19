name = str(input("Welcom to ^Make the wrong choices and you die^ Today you will be tested on 6 life or death questions. What is your name?:"))
health = 1

while health > 0:
  action = str(input('You enter a room because you are being chased by a tiger. You close the door behind you and are immediately locked inside. There are two doors. The first door has a pit full of lava. There is also a boat and an oar. The second door has a pit full of freezing cold water. There is also a boat and an oar. Which door do you choose? Type help to see options agian.'))
  if action == 'help':
      print('door 1, door 2,')
  elif action == 'door 1':
      print('You made the wrong choice. You try to cross the pit with the boat but it melts and you burn. Yay!')
      health = health - 1
      print (health)
  elif action == 'door 2':
      print ('You made the right choice. You use the boat and oar to cross the pit.')
      break

while health > 0:
  action = str(input('As soon as you cross the pit you find two more doors. Behind the first door is a hungry zombie. Behind the second door is a group of hungry tigers who didnt eat lunch. Which door do you choose? Type help to see options again.'))
  if action == 'help':
      print('door 1, door 2')
  elif action == 'door 1':
      print('You made the right choice. Zombies are not real.')
      break
  elif action == 'door 2':
      print ('You made the wrong choice. The tigers devour you. Yay!')
      health = health - 1
      print (health)
      
while health > 0:
  action = str(input('After you pass through the empty room without a zombie, you see two portals. The first portal has a serum that will turn you into a vampire. The second portal has a serum that will turn you into an animal. Which portal do you choose? Type help to see options again.'))
  if action == 'help':
      print('portal 1, portal 2')
  elif action == 'portal 1':
      print('You made the wrong choice. You drink the serum and turn into a vampire. Zombies are not real but vampires are in this game!')
      health = health - 1
      print (health)
  elif action == 'portal 2':
      print ('You made the right choice. You drink the serum and nothing happens because humans are animals.')
      break
      
while health > 0:
  action = str(input('After you drink the serum, you find another portal. It takes you to another room with 3 doors. Behind the first door is a volcano that will erupt as soon as you step foot inside. Behind the second door is a pit full of water and pirahnas. Behind the third door is a room with electric wires hanging on the walls. Which door do you choose? Type help to see options.'))
  if action == 'help':
      print('door 1, door 2, door 3')
  elif action == 'door 1':
      print ('You made the wrong choice. The volcano erupts and you are covered with burning ash.')
      health = health - 1
      print (health)
  elif action == 'door 2':
      print ('You made the wrong choice. The piranhas eat you alive.')
      health = health - 1
      print (health)
  elif action == 'door 3':
      print ('You made the right choice. The electric wires are hanging from the walls so you crawl under them.')
      break

while health > 0:
  action = str(input('After you crawl under the last wire the ground beneath you falls. You land on a coushin and see a sticky note. It says Drink one of the three drinks. The other two have POISON in them. 3 drinks magically appear in front of you. The first drink is lemonade that is 3 hours old. The second drink is hot tea. The third drink is ice cold lemonade. Which drink do you choose? Type help to see options again.'))
  if action == 'help':
      print('drink 1, drink 2, drink 3')
  elif action == 'drink 1':
      print('You made the wrong choice. The poison was in the ice and the it melted because the lemone was 3 hours old. The poison kills you.')
      health = health - 1
      print (health)
  elif action == 'drink 2':
      print ('You made the wrong choice. The poison was in the ice and it melted because of the hot tea. The poison kills you.')
      health = health - 1
      print (health)
  elif action == 'drink 3':
      print ('You made the right choice. The poison was in the ice and since it had not melted when you drank it you did not die.')
      health = health + 2
      break

while health > 0:
  action = str(input('When your tasty lemonade is finally finished a mysterious voice starts talking. It says, This is your final test. It will be your hardest one. Listen closely. What is fun to do but hard at the same time. Stressful but intelligent. Simple but indepth. Confusing but straightforward. If you answer this question you can leave. You have 3 tries. The answer is one word. No caps. What is your guess?'))
  if action == 'help':
      print('type one word answer. no caps')
  elif action == 'coding':
      print('WOW! Congratulations on solving this riddle. You may now leave.')
      break
  else:
      print ('No. Wrong answer. You lose 1 shot.')
      health = health - 1
      
