print("Hello. Today you will be put into one the the four harry potter houses. For more information about the houses use the know it all, GOOGLE.")
brain = 1
g = 0
s = 0
r = 0
h = 0
a = 0

while brain > 0:
    action = str(input('Out of these colors, which color do you like best? Red and Gold, Green and Silver, Yellow and Black, or Blue and Bronze? Type the first letter in no caps and no spaces of the two colors. :'))
    if action == 'rg':
      print('Ok. Answer added to database.')
      g = g + 1
      print (g)
      print (s)
      print (h)
      print (r)
      break
    if action == 'gs':
        print('Ok. Answer added to database.')
        s = s + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'yb':
        print('Ok. Answer added to database.')
        h = h + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'bb':
        print('Ok. Answer added to database.')
        r = r + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
        
while brain > 0:
    action = str(input('Which of these elements do you like the most? Air, Earth, Fire, or Water? : '))
    if action == 'Fire':
      print('Ok. Answer added to database.')
      g = g + 1
      print (g)
      print (s)
      print (h)
      print (r)
      break
    if action == 'Water':
        print('Ok. Answer added to database.')
        s = s + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Earth':
        print('Ok. Answer added to database.')
        h = h + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Air':
        print('Ok. Answer added to database.')
        r = r + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break

while brain > 0:
    action = str(input('Which of these traits are most like you - BE HONEST. 1. Hard work, patience, loyalty, and fair play. 2. Bravery, helping others, and chivalry. 3. Ambition, cunningness, heritage, and resourcefulness. 4. Intelligence, knowledge, planning ahead, and wit. Type in answer as 1/2/3/4: '))
    if action == '1':
      print('Ok. Answer added to database.')
      h = h + 1
      a = a + 1
      print (g)
      print (s)
      print (h)
      print (r)
      break
    if action == '2':
        print('Ok. Answer added to database.')
        g = g + 1
        a = a + 2
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == '3':
        print('Ok. Answer added to database.')
        s = s + 1
        a = a + 3
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == '4':
        print('Ok. Answer added to database.')
        r = r + 1
        a = a + 4
        print (g)
        print (s)
        print (h)
        print (r)
        break

while brain > 0:
    action = str(input('Which of these animals do you like the most? Badger, Serpent, Lion, or Raven. Type in answer as animal. : '))
    if action == 'Badger':
        print('Ok. Answer added to database.')
        h = h + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Serpent':
        print('Ok. Answer added to database.')
        s = s + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Lion':
        print('Ok. Answer added to database.')
        g = g + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Raven':
        print('Ok. Answer added to database.')
        r = r + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break


while brain > 0:
    action = str(input('If you were to choose which house would you choose? : '))
    if action == 'Gryffindor':
        print('Ok. Answer added to database.')
        g = g + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Slytherin':
        print('Ok. Answer added to database.')
        s = s + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Hufflepuff':
        print('Ok. Answer added to database.')
        h = h + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break
    if action == 'Ravenclaw':
        print('Ok. Answer added to database.')
        r = r + 1
        print (g)
        print (s)
        print (h)
        print (r)
        break


while brain > 0:
    if g > 2 and g < 6:
        print("Based on the questions you have been given you are in the Gryffindor house. Your colors are red and gold. Your element is fire. Your animal is a lion. You are brave, you like helping others, and have chivalry. A famous person from your house are Harry Potter, Ron Weasley, and Hermione Granger. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if s > 2 and s < 6:
        print("Based on the questions you have been given you are in the Slytherin house. Your colors are green and silver. Your element is water. Your animal is a serpent. You are ambitous, cunning, resourcefull, and belive in heritage. People from your house are Tom Riddle or Voldemort, Draco Malfoy, and Severus Snape. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if h > 2 and h < 6:
        print("Based on the questions you have been given you are in the Hufflepuff house. Your colors are yellow and blue. Your element it earth. Your animal is a badger. You are hard working, patient, loyal, and believe in fair play. Someone from your house Cedric Diggory. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if r > 2 and r < 6:
        print("Based on the questions you have been given you are in the Ravenclaw house. Your colors are blue and bronze. Your element is air. Your animal is a raven. You are intelligent and knowledgable. You are known for planning ahead and your wit. People from your house are Gilderoy Lockhart and Luna Lovegood. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if g > 1 and g < 3 and s > 0 and s < 2 and h > 0 and h < 2 and r > 0 and r < 2:
        print("Based on the questions you have been given you are in the Gryffindor house. Your colors are red and gold. Your element is fire. Your animal is a lion. You are brave, you like helping others, and have chivalry. A famous person from your house are Harry Potter, Ron Weasley, and Hermione Granger. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if s > 1 and s < 3 and g > 0 and g < 2 and h > 0 and h < 2 and r > 0 and r < 2:
        print("Based on the questions you have been given you are in the Slytherin house. Your colors are green and silver. Your element is water. Your animal is a serpent. You are ambitous, cunning, resourcefull, and belive in heritage. People from your house are Tom Riddle or Voldemort, Draco Malfoy, and Severus Snape. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if h > 1 and h < 3 and s > 0 and s < 2 and g > 0 and g < 2 and r > 0 and r < 2:
        print("Based on the questions you have been given you are in the Hufflepuff house. Your colors are yellow and blue. Your element it earth. Your animal is a badger. You are hard working, patient, loyal, and believe in fair play. Someone from your house Cedric Diggory. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if r > 1 and r < 3 and s > 0 and s < 2 and h > 0 and h < 2 and g > 0 and g < 2:
        print("Based on the questions you have been given you are in the Ravenclaw house. Your colors are blue and bronze. Your element is air. Your animal is a raven. You are intelligent and knowledgable. You are known for planning ahead and your wit. Remember these characteristics may not be the ones you chose but majority of them are.")
        break
    if g > 1 and g < 3 and s > 1 and s < 3:
        if a > 1 and a < 3:
            print("Based on the questions you have been given you are in the Gryffindor house. Your colors are red and gold. Your element is fire. Your animal is a lion. You are brave, you like helping others, and have chivalry. Remember these characteristics may not be the ones you chose but majority of them are.")
            break
        if a > 2 and a < 4:
            print("Based on the questions you have been given you are in the Slytherin house. Your colors are green and silver. Your element is water. Your animal is a serpent. You are ambitous, cunning, resourcefull, and belive in heritage. People from your house are Tom Riddle or Voldemort, Draco Malfoy, and Severus Snape.  Remember these characteristics may not be the ones you chose but majority of them are.")
            break
    if g > 1 and g < 3 and r > 1 and r < 3:
        if a > 1 and a < 3:
            print("Based on the questions you have been given you are in the Gryffindor house. Your colors are red and gold. Your element is fire. Your animal is a lion. You are brave, you like helping others, and have chivalry. A famous person from your house are Harry Potter, Ron Weasley, and Hermione Granger. Remember these characteristics may not be the ones you chose but majority of them are.")
            break
        if a > 3 and a < 5:
            print("Based on the questions you have been given you are in the Ravenclaw house. Your colors are blue and bronze. Your element is air. Your animal is a raven. You are intelligent and knowledgable. You are known for planning ahead and your wit.")
            break
    if g > 1 and g < 3 and r > 1 and r < 3:
        if a > 1 and a < 3:
            print("Based on the questions you have been given you are in the Gryffindor house. Your colors are red and gold. Your element is fire. Your animal is a lion. You are brave, you like helping others, and have chivalry. A famous person from your house are Harry Potter, Ron Weasley, and Hermione Granger.")
            break
        if a > 0 and a < 2:
            print("Based on the questions you have been given you are in the Hufflepuff house. Your colors are yellow and blue. Your element it earth. Your animal is a badger. You are hard working, patient, loyal, and believe in fair play. Someone from your house Cedric Diggory.")
            break
    if s > 1 and s < 3 and r > 1 and r < 3:
        if a > 2 and a < 4:
            print("Based on the questions you have been given you are in the Slytherin house. Your colors are green and silver. Your element is water. Your animal is a serpent. You are ambitous, cunning, resourcefull, and belive in heritage. People from your house are Tom Riddle or Voldemort, Draco Malfoy, and Severus Snape.")
            break
        if a > 3 and a > 5:
            print("Based on the questions you have been given you are in the Ravenclaw house. Your colors are blue and bronze. Your element is air. Your animal is a raven. You are intelligent and knowledgable. You are known for planning ahead and your wit.")
            break
    if s > 1 and s < 3 and h > 1 and h < 3:
        if a > 2 and a < 4:
            print("Based on the questions you have been given you are in the Slytherin house. Your colors are green and silver. Your element is water. Your animal is a serpent. You are ambitous, cunning, resourcefull, and belive in heritage. People from your house are Tom Riddle or Voldemort, Draco Malfoy, and Severus Snape.")
            break
        if a > 0 and a < 2:
            print("Based on the questions you have been given you are in the Hufflepuff house. Your colors are yellow and blue. Your element it earth. Your animal is a badger. You are hard working, patient, loyal, and believe in fair play. Someone from your house Cedric Diggory.")
            break
    if h > 1 and h < 3 and r > 1 and r < 3:
        if a > 0 and a < 2:
            print("Based on the questions you have been given you are in the Hufflepuff house. Your colors are yellow and blue. Your element it earth. Your animal is a badger. You are hard working, patient, loyal, and believe in fair play. Someone from your house Cedric Diggory.")
            break
        if a > 3 and a > 5:
            print("Based on the questions you have been given you are in the Ravenclaw house. Your colors are blue and bronze. Your element is air. Your animal is a raven. You are intelligent and knowledgable. You are known for planning ahead and your wit.")
            break
    
    