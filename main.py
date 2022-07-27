# [x] paint 10 x 10 rows and spots
# [x] each dot is 20 in size, spaced by 50

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
                    (27, 40, 157)]

#TODO: Import Turtle and Random
import turtle as t
import random

#TODO: Create our cursor shape, size, speed
hirst = t.Turtle()
hirst.penup()
coords = -250
hirst.ht()

#TODO: Set the random colors based on final color list
window = t.Screen()
window.colormode(255)

#TODO: Create a function that paints the 10 x 10
def rows():
    hirst.setpos(-250, coords)
    for x in range(10):
        current_item = random.choice(color_list)
        hirst.dot(20, current_item)
        hirst.forward(50)

#TODO: Execute
for x in range(10):
    rows()
    coords += 50

#TODO: Set up Screen to exit
window.exitonclick()



