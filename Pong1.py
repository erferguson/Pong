# Simple Pong in Python3

import turtle  # built-in Python, starter for Games, good for Beginners

wn = turtle.Screen()
wn.title('Pong by Eric Ferguson')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) # stops the window from Updating, means a Manual Update now

# Paddle A > on LEFT
a_paddle = turtle.Turtle()
a_paddle.speed(0)
a_paddle.shape('square')
a_paddle.color('yellow')
a_paddle.shapesize(stretch_wid=5, stretch_len=1)
a_paddle.penup()
a_paddle.goto(-350, 0) # set starting position of a_paddle

# Paddle B > on RIGHT
b_paddle = turtle.Turtle()
b_paddle.speed(0)
b_paddle.shape('square')
b_paddle.color('gray')
b_paddle.shapesize(stretch_wid=5, stretch_len=1)
b_paddle.penup()
b_paddle.goto(350, 0) # set starting position of b_paddle

# Ball > CENTERED
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0, 0) # set starting position of ball
ball.dx = 2 #delta ?
ball.dy = -2 # everytime ball moves it moves 2 pixles

# Function > A_Paddle UP
def a_paddle_up():
    y = a_paddle.ycor() # returns y coordinate, assign to y
    y += 20 # adds Pixels to Y coordinate
    a_paddle.sety(y)

# Function > A_Paddle DOWN
def a_paddle_down():
    y = a_paddle.ycor() # returns y coordinate, assign to y
    y -= 20 # adds Pixels to Y coordinate
    a_paddle.sety(y)

    # Function > B_Paddle UP
def b_paddle_up():
    y = b_paddle.ycor() # returns y coordinate, assign to y
    y += 20 # adds Pixels to Y coordinate
    b_paddle.sety(y)

# Function > B_Paddle DOWN
def b_paddle_down():
    y = b_paddle.ycor() # returns y coordinate, assign to y
    y -= 20 # adds Pixels to Y coordinate
    b_paddle.sety(y)

# Keyboard binding ?
wn.listen()
wn.onkeypress(a_paddle_up, 'e')
wn.onkeypress(a_paddle_down, 'd')

wn.onkeypress(b_paddle_up, 'Up')
wn.onkeypress(b_paddle_down, 'Down')


# Main Game Loop
while True: 
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Y coordinate
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of the Ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of the Ball

    # X coordinate
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < b_paddle.ycor() + 40 and ball.ycor() > b_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a_paddle.ycor() + 40 and ball.ycor() > a_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1