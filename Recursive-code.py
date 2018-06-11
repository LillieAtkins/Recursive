import turtle
import random

def drawTree(length):
    """
    This takes the starting length and turns it into a tree with a random length of branches and angles. The width of the branches changes based on the length and the color changes to green when the length is smaller than 30. 
    """
    a = random.randint(0,50)
    b = random.randint(0,50)
    m = length+random.randint(-length//10, length//10)
    if length <= 10: #no else as this is an implicite base case because you are saying to do nothing if the gen is less than one (or could write an else with pass as the action, which means do nothing)
        return
    else:
        if length > 30:
            turtle.pencolor('brown')
        else:
            turtle.pencolor('green')
        turtle.width(length//7)
        turtle.forward(m) #draw trunk 
        turtle.right(a)
        drawTree(m*0.8) # draw right substree
        turtle.left(a) # undo right turn
        turtle.left(b) # random left turn
        drawTree(m*0.8) # draw left subtree
        turtle.right(b) # undo left turn
        turtle.penup()
        turtle.backward(m)   # puts turtle back to the start
        turtle.pendown()
        
def drawTreeScene():
    """ 
    Moves the turtle to the bottom of the screen, points it upward draws a tree, then moves the turtle to a location on the bottom right of the screen and draws a second tree, and then again moves the turtle this time to the bottom left of the screen and draws a third tree. 
    """
    # turn off drawing animation (too slow otherwise)
    turtle.tracer(False)
        
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    turtle.penup()
    turtle.goto(0, -turtle.window_height()/2 + 20)
    turtle.left(90)
    turtle.pendown()    

    # draw the tree by calling your function
    drawTree(150)
    turtle.penup()
    turtle.goto(450,-300)
    turtle.pendown()
    drawTree(100)
    turtle.penup()
    turtle.goto(-450, -350)
    turtle.pendown()
    drawTree(50)


    # finished
    turtle.update()
    turtle.done()
    

def drawSierpinski(length, iterations):
    """
    This takes the length and iterations to draw a the Sierpinski triangle pattern.
    """
    if iterations == 1:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
    else:
        drawSierpinski(length/2, iterations-1)
        turtle.forward(length/2)
        drawSierpinski(length/2, iterations-1)
        turtle.left(120)
        turtle.forward(length/2)
        turtle.right(120)
        drawSierpinski(length/2, iterations-1)
        turtle.right(120)
        turtle.forward(length/2)
        turtle.left(120)
        
        #call last iteration and draw it three times
        
    

def drawSierpinskiScene(length, iterations):
    """
    This moves the turtle to the right side of the screen and takes the length and iterations and feds them into the drawSierpinski() function.
    """

    # turn off animation (too slow otherwise)
    turtle.tracer(False)

	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    turtle.penup()
    turtle.goto(-turtle.window_width()/3 + 20,0)
    turtle.pendown()
	
    drawSierpinski(length, iterations)
    
    # finish
    turtle.update()
    turtle.done()
    
def drawcarpet(length, gen):
    """
    This function takes the length and generations to draw a Sierpinski carpet pattern.
    """
    if gen == 0:
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.end_fill()
    else:
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        turtle.left(90)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        turtle.left(90)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(length/3)
        turtle.left(90)
        turtle.forward(length/3)
        drawcarpet(length/3, gen-1)
        turtle.forward(2*length/3)
        turtle.left(90)

def drawcarpetscene(length, gen):
    """
    This moves the turtle to the right side of the page and then calls the drawcarpet() function and feds the length and generations entered into this.
    """
        # turn off animation (too slow otherwise)
    turtle.tracer(False)

	
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    turtle.penup()
    turtle.goto(-turtle.window_width()/3 + 20,-40)
    turtle.pendown()
	
    drawcarpet(length, gen)
    
    # finish
    turtle.update()
    turtle.done()
