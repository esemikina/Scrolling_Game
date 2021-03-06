######################################################
# Project: A Scrolling Game
# UIN: 670246811
# repl.it URL: https://trinket.io/library/trinkets/4ca638dcb4
######################################################
#!/bin/python3

# # imports
import turtle 
import random
import math

# Globals Declaration
alien = None
human = None
meteorite = None
screen = None
screen_width = None
screen_height = None
game_over = None

lives = None
score = None
radius = None
alienRadius = None
game_over = False

# Initialization
screen_width = 500
screen_height = 500
lives = 3
score = 0
radius = 5
alienRadius = 6
alien = turtle.Turtle() 
human = turtle.Turtle()
meteorite = turtle.Turtle()


screen = turtle.Screen()
screen.setup(screen_width,screen_height)
# screen.setworldcoordinates(-100, 0, -100, 195)
screen.bgpic("space.png")

#AlienImage
AlienImage = "alien1.png"

#Adding Alien Image and setting it up
screen.addshape(AlienImage)
alien.shape(AlienImage)
alien.hideturtle()
alien.speed(1000)
alien.setpos(-205, 200)
alien.showturtle()

#HumanImage
HumanImage = "human1.png"

# Adding Human Image and setting it up
screen.addshape(HumanImage)
human.shape(HumanImage)
human.hideturtle()
human.speed(1000)
human.setpos(250,170)
human.showturtle()

#MeteoriteImage
MeteoriteImage = "meteor.png"

# Adding Meteorite Image and setting it up
screen.addshape(MeteoriteImage)
meteorite.shape(MeteoriteImage)
meteorite.hideturtle()
meteorite.speed(1000)
meteorite.setpos(255,0)
meteorite.showturtle()

#speed for moving
move_speed = 10


#Player moves up and down
def up():
  alien.sety( int(alien.ycor()) + move_speed )

 
def down():
 alien.sety( int(alien.ycor()) - move_speed )

def collides(obj1, obj2):
  dist = math.sqrt(abs((obj1.position()[0] - obj2.position()[0])**2 - (obj1.position()[1] - obj2.position()[1])**2))
  if abs(int(dist)) < alienRadius + radius and abs(int(dist)) > 0:
    return True
  else:
    return False
 

# now associate the defs from above with certain keyboard events
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

screen.tracer(0)



#Meteorite and Human moves from right to left
while True: 
  if game_over == False:
    turtle.clear()
    turtle.setposition(0, 200)  # In this position I want to output variable
    turtle.write('Score: '+str(score)+' - Lives: '+str(lives), font=("Arial", 16, "normal"), align='center')
    turtle.color('deep pink')
    screen.update()   
    turtle.hideturtle()
    
    
    
    meteorite.backward(3)
    human.backward(3)
    
    if(collides(alien, human) == True):
        score += 4
        human.setpos(250, random.randint(0,225))
    
    if(collides(alien, meteorite) == True):
        lives -= 1
        meteorite.setpos(250, random.randint(0,225))
        if lives == 0:
          game_over = True
    
    if meteorite.position()[0] < -250:
      meteorite.setpos(250, random.randint(0,205))
      
    if human.position()[0] < -250:
      human.setpos(250, random.randint(0,205))
      
    if alien.position()[1] < -225:
      alien.setpos(-205, 220)
      
    if alien.position()[1] > 225:
     alien.setpos(-205, -225)
  else:
    turtle.clear()
    turtle.penup()
    turtle.setposition(0, 0)  # In this position I want to output variable
    turtle.pendown()
    turtle.write('Game Over!', font=("Arial", 16, "normal"), align='center')
    turtle.color('deep pink')
    screen.update()  
    turtle.hideturtle()









 









 