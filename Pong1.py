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

# Main Game Loop
while True: 
    wn.update()