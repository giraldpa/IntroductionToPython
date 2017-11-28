"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Pattie Giraldo.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

windows = rg.TurtleWindow()

green_turtle = rg.SimpleTurtle('turtle')
green_turtle_pen = rg.Pen('green', 10)
green_turtle.pen = green_turtle_pen
green_turtle.speed = 100

pink_turtle = rg.SimpleTurtle()
pink_turtle_pen = rg.Pen('pink', 5)
pink_turtle.pen = pink_turtle_pen
pink_turtle.speed = 15

for k in  range(17):


    green_turtle.draw_regular_polygon(10, 50)
    green_turtle.pen_up()
    green_turtle.right(20)
    green_turtle.pen_down()

for k in range(5):

    pink_turtle.draw_square(10)
    pink_turtle.pen_up()
    pink_turtle.forward(50)
    pink_turtle.pen_down()





