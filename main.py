from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Game")
screen.tracer(0)

paddle = Paddle()
top_ball = Ball((random.randint(-260, 260), 270))
move_ball = Ball((0, -220))
scoreboard = Scoreboard()

# Move paddle
screen.listen()
screen.onkey(paddle.right_move, "Right")
screen.onkey(paddle.left_move, "Left")

run = True
while run:
    time.sleep(0.1)
    screen.update()
    move_ball.move()

    # Check live
    if scoreboard.live == 0:
        run = False
        scoreboard.game_over()
    
    # Collision with xcor
    if move_ball.xcor() > 280 or move_ball.xcor() < -280:
        move_ball.bounce_x()
        
    # Collision with ycor
    if move_ball.ycor() > 280:
        move_ball.bounce_y()  
        
    # Collision with paddle
    if move_ball.distance(paddle) < 30:
        move_ball.bounce_y()  

    # Collision with ball to increase the score
    if move_ball.distance(top_ball) < 15:
        top_ball.random_move()
        scoreboard.increase_score()
        
    # Collision with bottom y
    if move_ball.ycor() < -290:
        move_ball.reset_position()
        scoreboard.decrease_live()


screen.exitonclick()