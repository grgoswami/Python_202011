import turtle
chang = turtle.Pen()
chang.shape('turtle')
chang.speed(0)

# Start drawing
chang.left(45)
for x in range(8):
    for y in range(8):
        isBlack = ((x + y) % 2 == 0) 
                            
        # Move to new position.
        chang.penup()
        chang.goto(-256 + 70.71 * x, -256 + 70.71 * y)
        chang.pendown()

        # Draw one small squre and decide to fill it or not.
        if isBlack:
            chang.begin_fill()
        chang.circle(50,steps=4)
        if isBlack:
            chang.end_fill()

chang.hideturtle()

        
