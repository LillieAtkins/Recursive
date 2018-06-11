import turtle

def drawSquare(length):
    """
    Draw a square with sides of size length.
    """
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    
def drawSquareScene():
    """
    Helper function to call drawSquare() function.
    """
    drawSquare(100)
    turtle.done()

def drawKoch(length, gen):
    """
    Draw Koch curve of overall length length and generation gen.
    """
    if gen == 0:
        turtle.forward(length)
    else: #this does gen 1, gen 2, gen 3...
        drawKoch(length/3, gen-1) #this is the recursive curve
        turtle.left(60)
        drawKoch(length/3, gen-1)
        turtle.right(120)
        drawKoch(length/3, gen-1)
        turtle.left(60)
        drawKoch(length/3, gen-1)
        

def drawKochScene(L, g): #can get rid of these parameters and go down lower and just set what it will draw or can leave like this so you call what you want
    """
    Setup the canvas for drawing the curve and draw it
    """ #this will call drawKoch
	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(-turtle.window_width()/2 + 20,0) #move over to the edge but moves you slightly out
    turtle.pendown()    
    
    # draw the curve by calling your function
    drawKoch(L, g)
    
    # finished
    turtle.done()

def drawSnowflake(length, generations):
    """
    This takes the size and generation of the koch curve to draw the koch curve as the sides of an equilateral triangle.
    """
    drawKoch(length, generations)
    turtle.right(120)
    drawKoch(length, generations)
    turtle.right(120)
    drawKoch(length, generations)
    turtle.right(120)
    
def drawSnowflakeScene():
    """
    This takes no input and draws three snowflakes all of different sizes and in different locations, with no connecting lines.
    """
    turtle.fillcolor('red')
    turtle.begin_fill()
    drawSnowflake(50, 3)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(100)
    turtle.fillcolor('yellow')
    turtle.pencolor('green')
    turtle.pendown()
    turtle.begin_fill()
    drawSnowflake(100,2)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-100, -200)
    turtle.fillcolor('pink')
    turtle.pencolor('purple')
    turtle.pendown()
    turtle.begin_fill()
    drawSnowflake(25,1)
    turtle.end_fill()
    
def reverse(text):
    """
    This function takes a string and reverses the characters in it.
    """
    if text == '':
        return ''
    else:
        return reverse(text[1:]) + text[0]
    
def spiral(initialLength, angle, multiplier):
    """
    This takes an integer length, an angle, and a multipler to create a spiral.
    """
    turtle.tracer(False)
    turtle.update()
    if initialLength <= 1 or initialLength >= 1000:
        return #empty return just means stop
    else:
        turtle.forward(initialLength)
        turtle.right(angle)
        return spiral(initialLength*multiplier, angle, multiplier) 
    
def drawSpiralScene():
    """
    This function takes no arguments and draws three different spirals.
    """
    turtle.tracer(False)
    turtle.penup()
    turtle.pencolor('pink')
    turtle.backward(120)
    turtle.left(70)
    turtle.forward(130)
    turtle.pendown()
    spiral(50, 13, .97)
    
    turtle.penup()
    turtle.pencolor('blue')
    turtle.forward(380)
    turtle.right(70)
    turtle.forward(20)
    turtle.pendown()
    spiral(150,120,.8)
    
    turtle.penup()
    turtle.pencolor('purple')
    turtle.goto(160,-120)
    turtle.pendown()
    spiral(180, 92, .95) # challenge spiral
    turtle.update()
