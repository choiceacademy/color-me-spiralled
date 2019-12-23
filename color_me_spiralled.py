# ColorSpiralInput.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
# Set up a list of any 8 valid Python color names
colors = ["red", "yellow", "blue", "green",
          "orange", "purple", "white", "gray"]
# Ask the user's name using turtle's text input pop-up window and the number of sides they would like
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int( turtle.numinput("Number of sides","How many sides do you want (1-8)?", 4, 1, 8))
# Draw a colorful spiral with the user-specified number of sides
for x in range(300):
    t.pencolor( colors[ x % sides] )
    t.penup()
    t.forward( x * sides )
    t.pendown()
    t.write(your_name, font = ("Times", int( (x + 4) / 4), "bold") )
    t.left(360/sides+1)
 
