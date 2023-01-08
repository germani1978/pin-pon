from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from score import ScoreBoard
import time

#pantalla
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pin Pon')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

on_game = True
while on_game:
    ball.move()
    time.sleep(0.1)
    screen.update()
    
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bouncex() 
        
    if ball.distance(r_paddle) < 50 and  ball.xcor() > 320  or ball.distance(l_paddle) < 50 and  ball.xcor() < -320:
        ball.bouncey()  
        
    if ball.xcor() > 390:
         ball.reset_position()
         scoreboard.r_point()
    
    if ball.xcor() < -390:
         ball.reset_position() 
         scoreboard.l_point()
        


screen.exitonclick()