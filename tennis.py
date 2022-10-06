#tennis game - priyal shah
import turtle
import random
from playsound import playsound

#this is to generate random tennis player names for the left and right players OR to let players choose
print("randomly choose tennis players or enter names")
print("\t a) randomly choose")
print("\t b) enter")
choice = str(input())

if choice == 'a':
#this is to generate random tennis player names for the left and right players 
    players = ["Medvedev", "Tashjian", "Marfeo", "Nadal", "Alcaraz", "Shelton", "Ruud", "Norrie", "Hurkacz", "Rublev", "Fritz", "Kyrgios", "Kokkinakis", "Tiafoe", "Swiatek", "Sakkari", "Jabeur", "Sabalenka", "Pegula", "Fernandez", "Sinner", "Gauff", "Nakashima", "Keys"]
    playerL = players[random.randint(0, len(players)-1)]
    playerR = players[random.randint(0, len(players)-1)]

    while(playerL == playerR): #making sure the players aren't the same
        playerR = players[random.randint(0, len(players)-1)]
else:
    playerL = str(input("Enter player 1: "))
    playerR = str(input("Enter player 2: "))
                     
#background
sc = turtle.Screen()
sc.title("Tennis Game")
sc.bgcolor("medium sea green")
sc.setup(width=1000, height=600)
#making the tennis court lines w/ turtle
x = turtle.Turtle()
x.speed(0)
x.color("white", "royal blue")
x.shape("square")
x.shapesize(stretch_wid=20, stretch_len=40)
x.penup()
x.goto(0,0)
y = turtle.Turtle()
y.speed(0)
y.color("white", "royal blue")
y.shape("square")
y.shapesize(stretch_wid=20, stretch_len=20)
y.penup()
y.goto(0,0)
z = turtle.Turtle()
z.speed(0)
z.color("white", "royal blue")
z.shape("square")
z.shapesize(stretch_wid=5, stretch_len=40)
z.penup()
z.goto(0,150)
a = turtle.Turtle()
a.speed(0)
a.color("white", "royal blue")
a.shape("square")
a.shapesize(stretch_wid=5, stretch_len=40)
a.penup()
a.goto(0,-150)
c = turtle.Turtle()
c.speed(0)
c.color("white", "royal blue")
c.shape("square")
c.shapesize(stretch_wid=5, stretch_len=10)
c.penup()
c.goto(100,50)
d = turtle.Turtle()
d.speed(0)
d.color("white", "royal blue")
d.shape("square")
d.shapesize(stretch_wid=5, stretch_len=10)
d.penup()
d.goto(-100,50)
#this is to make the net
b = turtle.Turtle()
b.speed(0)
b.color("white")
b.shape("square")
b.shapesize(stretch_wid=20, stretch_len=0.5)
b.penup()
b.goto(0,0)



#left paddle
image = ("racket3.gif")
sc2 = turtle.Screen()
sc2.addshape(image)
left_pad = turtle.Turtle()
left_pad.speed(10)
left_pad.shape(image)
left_pad.color("white", "blue")
#left_pad.shapesize(stretch_wid=0.01, stretch_len=0.01)
left_pad.penup()
left_pad.goto(-425, 0)


#right paddle
right_pad = turtle.Turtle()
right_pad.speed(10)
right_pad.shape(image)
right_pad.color("blue", "white")
#right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(425, 0)


#ball
hit_ball = turtle.Turtle()
hit_ball.speed(10)
hit_ball.shape("circle")
hit_ball.color("white", "yellow")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.vx = 100
hit_ball.dy = -5
hit_ball.vy = 100


#score
left_player = 0
right_player = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("ghost white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(playerL + ": 0" + " " + playerR + ": 0", align="center", font=("Garamond", 24, "normal"))


#making paddle moves
def paddleaup():
	y = left_pad.ycor()
	y += 20
	left_pad.sety(y)
def paddleadown():
	y = left_pad.ycor()
	y -= 20
	left_pad.sety(y)
def paddlebup():
	y = right_pad.ycor()
	y += 20
	right_pad.sety(y)
def paddlebdown():
	y = right_pad.ycor()
	y -= 20
	right_pad.sety(y)

#keyboard
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

#celebration fireworks!
t = turtle.Turtle()
t.speed(0)

def pen(color):
    t.color(color)

def move():
    t.pu()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.goto(x, y)
    t.pd()

def firework(size):
    for num in range(20):
        t.fd(size)
        t.rt(180-(360/20))


C_BRIGHT_MIN = 0x10
C_BRIGHT_MAX = 0xef
F_SIZE_MIN = 15
F_SIZE_MAX = 200
FIREWORK_PER_CLEAR = 2

def firework3():
    while True:
        color_r = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        color_g = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        color_b = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
        pen('#'+color_r+color_g+color_b)
        for i in range(FIREWORK_PER_CLEAR):
            firework(random.randint(F_SIZE_MIN, F_SIZE_MAX))
            move()
        t.clear()

#function for when a player wins
def celebration(num):
    sc.clear()
    win = turtle.Screen()
    win.title("Win Screen")
    win.bgcolor("thistle")
    win.setup(width=1000, height=600)
    sketch.clear()
    sketch.goto(0, 0)
    if(num==1):
        sketch.write(playerR + " wins!!!", align="center", font=("Garamond", 100, "normal"))
    else:
         sketch.write(playerL + " wins!!!", align="center", font=("Garamond", 100, "normal"))
    playsound("TheMedvedevSpeech .mp3")
    firework3()

#making the game run!  
while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    #checking borders
    if hit_ball.ycor() > 280:
            hit_ball.sety(280)
            hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
            hit_ball.sety(-280)
            hit_ball.dy *= -1
            
    #if right misses it, with cases for diff score
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        if (left_player == 0):
            left_player = 15
        elif left_player == 15:
            left_player = 30
        elif(left_player == 30):
            left_player = 40
        elif(left_player == 40 and right_player == 40):
            left_player = 'AD'
        elif(right_player == 'AD' and left_player == 40):
            right_player = 40
        elif(left_player == 40 and right_player != 40):
            celebration(2)
            break
        elif(left_player == 'AD'):
            celebration(2)
            break
        sketch.clear()
        sketch.write(playerL + ": " + str(left_player) + " " + playerR + ": " + str(right_player), align="center", font=("Garamond", 24, "normal"))

    #if left misses it, with cases for diff score
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        if(right_player == 0):
            right_player = 15
        elif(right_player == 15):
            right_player = 30
        elif(right_player == 30):
            right_player = 40
        elif(right_player == 40 and left_player == 40):
            right_player = 'AD'
        elif(left_player == 'AD' and right_player == 40):
            left_player = 40
        elif(right_player == 40 and left_player != 40):
            celebration(1)
            break
        elif(right_player == 'AD'):
            celebration(1)
            break
        sketch.clear()
        sketch.write(playerL + ": " + str(left_player) + " "  + playerR + ": " + str(right_player), align="center", font=("Garamond", 24, "normal"))

    #when ball hits paddle...
    if (hit_ball.xcor() > 390 and hit_ball.xcor() < 400) and (hit_ball.ycor() < right_pad.ycor()+100 and hit_ball.ycor() > right_pad.ycor()-100):
            hit_ball.setx(360)
            hit_ball.dx*=-1
            playsound("bounce.mp3")
            
    if (hit_ball.xcor()<-390 and hit_ball.xcor()>-400) and (hit_ball.ycor()<left_pad.ycor()+100 and hit_ball.ycor()>left_pad.ycor()-100):
            hit_ball.setx(-360)
            hit_ball.dx*=-1
            playsound("bounce.mp3")
