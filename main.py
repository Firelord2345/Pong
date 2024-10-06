from turtle import Screen
from paddle import Paddle  # Assuming Paddle class is in a separate file paddle.py
from ball import Ball      # Assuming Ball class is in a separate file ball.py
from score import Score    # Assuming Score class is in a separate file score.py
import time

# Initialize screen
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)

# Create paddles
r_block = Paddle((230, 0))  # Right paddle
l_block = Paddle((-230, 0))  # Left paddle
ball = Ball()                # Ball object
score = Score()              # Score object

# Listen for key presses
screen.listen()
screen.onkey(r_block.up, "Up")      # Move right paddle up with "Up" arrow key
screen.onkey(r_block.down, "Down")  # Move right paddle down with "Down" arrow key
screen.onkey(l_block.up, "w")       # Move left paddle up with "W" key
screen.onkey(l_block.down, "s")     # Move left paddle down with "S" key

# Main game loop
is_run = True
while is_run:
    screen.update()
    time.sleep(ball.speed1)  # Control ball speed dynamically
    ball.move()

    # Collision with top and bottom walls
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    # Detect collision with right paddle (r_block)
    if ball.distance(r_block) < 50 and ball.xcor() > 210:
        ball.bounce_x()

    # Detect collision with left paddle (l_block)
    if ball.distance(l_block) < 50 and ball.xcor() < -210:
        ball.bounce_x()

    # Ball passes the right boundary (right player misses)
    if ball.xcor() > 260:
        ball.reset_position()
        score.l_point()  # Left player scores a point

    # Ball passes the left boundary (left player misses)
    if ball.xcor() < -260:
        ball.reset_position()
        score.r_point()  # Right player scores a point

screen.exitonclick()
