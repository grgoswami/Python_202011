import turtle
fred = turtle.Pen()
fred.width(25)
colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
for i in range(0, 7):
  fred.penup()
  fred.goto(180 - i * 20 + 10, 0)
  fred.left(90)
  fred.color(colors[i])
  fred.pendown()
  fred.circle(radius=180 - i * 20, extent=180)
  fred.left(90)

	
 
