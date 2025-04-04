import turtle #importing library
turtle.Screen().bgcolor("orange") #changing background color
turtle.Screen().setup(300,400) #setting up the size of the screen
polygon = turtle.Turtle() #defining the variable

num_sides = 6 #defining the variable
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides): 
  polygon.forward(side_length)
  polygon.right(angle)
turtle.done()