import time
import turtle
import winsound
from playsound import playsound

# Setup Window
pong = turtle.Screen()
pong.title('Welcome to the One Pongch Man......Oh Wait')
pong.bgpic('pics\wall1.png')
pong.bgcolor('black')
pong.setup(width=1366, height=768)
pong.tracer(0)
pong.addshape('pics\wood12.gif')
pong.addshape('pics\wood8.gif')
pong.addshape('pics\wood6.gif')
pong.addshape('pics\woodframe.gif')



# Set up a rim so that when ppl want to play it in full screen they know where are the boundaries of the ball
rim_upper = turtle.Turtle()
rim_upper.speed(0)
rim_upper.penup()
rim_upper.shape('pics\woodframe.gif')
rim_upper.goto(0,365)


rim_lower = turtle.Turtle()
rim_lower.speed(0)
rim_lower.penup()
rim_lower.shape('pics\woodframe.gif')
rim_lower.goto(0,-365)



# Play My BGM Music!!
winsound.PlaySound('sounds\BGM.wav', winsound.SND_LOOP + winsound.SND_ASYNC)


# Setup the score title, but do not write on it yet.
title = turtle.Turtle()
title.speed(0)
title.color('white')
title.penup()
title.hideturtle()
title.goto(0,320)
title.clear()

# Exit Message: constantly show this message at the bottom right corner
message = turtle.Turtle()
message.speed(0)
message.color('white')
message.penup()
message.hideturtle()
message.goto(400,-320)
message.write("                        Press 'Esc' to quit\n"
              "     'w' and 's' to control the left paddle\n"
              "'up' and 'down' to control the right paddle",  align='center',font=('Courier', 15,'normal') )





# Game Over Notice
gonotice = turtle.Turtle()
gonotice.speed(0)
gonotice.color('white')
gonotice.goto(0,0)
gonotice.penup()
gonotice.hideturtle()
gonotice.clear()

# Paddle A in the left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('pics\wood12.gif')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=12, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-500,0)

# Paddle B in the right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('pics\wood12.gif')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=12, stretch_len=1)
paddle_b.penup()
paddle_b.goto(500,0)

# Ball
ball = turtle.Turtle()
ball.size = 2.0
ball.speed(0)
ball.shape('circle')
ball.shapesize(stretch_wid= ball.size , stretch_len= ball.size)
ball.color('white')
ball.goto(0,0)
ball.penup()
ball.velocity = 0.67


# Ball2
ball_2 = turtle.Turtle()
ball_2.speed(0)
ball_2.shape('circle')
ball_2.shapesize(stretch_wid= ball.size , stretch_len= ball.size)
ball_2.color('yellow')
ball_2.penup()
ball_2.goto(0,1000)


# Ball3
ball_3 = turtle.Turtle()
ball_3.speed(0)
ball_3.shape('circle')
ball_3.shapesize(stretch_wid= ball.size , stretch_len= ball.size)
ball_3.color('pink')
ball_3.penup()
ball_3.goto(0,1000)


# Ball4
ball_4 = turtle.Turtle()
ball_4.speed(0)
ball_4.shape('circle')
ball_4.shapesize(stretch_wid= ball.size , stretch_len= ball.size)
ball_4.color('grey')
ball_4.penup()
ball_4.goto(0,1000)



# Variables Here
pong.bounce_length = 123
pong.paddle_length = 12
pong.paddle_speed = 30

title.score = 0
title.lvl = 1
title.write('Your Score: {}     Current Level: {}'.format(title.score,title.lvl), align='center',
            font=('Courier', 30,'normal'))
pong.switch1 = 0
pong.switch2 = 0
pong.switch3 = 0
pong.switch4 = 0

ball.dx = 2 * ball.velocity
ball.dy = 2 * ball.velocity
ball_2.dx = 0
ball_2.dy = 0
ball_3.dx = 0
ball_3.dy = 0
ball_4.dx = 0
ball_4.dy = 0

pong.running = 1

# Move the paddles!! Hooray!!
def paddle_a_up():
    if paddle_a.ycor() < 360 - pong.bounce_length - pong.paddle_speed:
        i = paddle_a.ycor()
        i = i + pong.paddle_speed
        paddle_a.sety(i)
    else:
        paddle_a.sety(360 - pong.bounce_length)

def paddle_b_up():
    if paddle_b.ycor() < 360 - pong.bounce_length - pong.paddle_speed:
        i = paddle_b.ycor()
        i = i + pong.paddle_speed
        paddle_b.sety(i)
    else:
        paddle_b.sety(360 - pong.bounce_length)



def paddle_a_down():
    if paddle_a.ycor() > pong.paddle_speed + pong.bounce_length - 360:
        i = paddle_a.ycor()
        i = i - pong.paddle_speed
        paddle_a.sety(i)
    else:
        paddle_a.sety(pong.bounce_length - 360)

def paddle_b_down():
    if paddle_b.ycor() > pong.paddle_speed + pong.bounce_length - 360:
        i = paddle_b.ycor()
        i = i - pong.paddle_speed
        paddle_b.sety(i)
    else:
        paddle_b.sety(pong.bounce_length - 360)




def quitgame():
    gonotice.clear()
    gonotice.write(' You have reached LVL {}!\n    Come Back Anytime'.format(title.lvl),
                   align='center', font=('Courier', 35, 'normal'))
    ball.clear()
    playsound('sounds\lvlup.wav',0)
    time.sleep(2)
    pong.running = 0



def restart():
    winsound.PlaySound(None,winsound.SND_ASYNC)
    winsound.PlaySound('sounds\BGM.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
    title.lvl = 1
    title.score = 0
    ball.size = 2.0
    pong.bounce_length = 123
    pong.paddle_length = 12
    paddle_a.shape('pics\wood12.gif')
    paddle_b.shape('pics\wood12.gif')
    pong.paddle_speed = 30
    gonotice.clear()
    ball.goto(0,0)
    title.clear()
    ball.velocity = 0.67
    ball.dx = 2 * ball.velocity
    ball.dy = 2 * ball.velocity
    title.write('Your Score: {}     Current Level: {}'.format(title.score, title.lvl), align='center',
                font=('Courier', 30, 'normal'))
    ball_3.dx = 0
    ball_3.dy = 0
    ball_4.dx = 0
    ball_4.dy = 0
    ball_4.goto(0,1000)
    ball_3.goto(0, 1000)
    ball_2.dx = 0
    ball_2.dy = 0
    ball_2.goto(0, 1000)
    pong.switch1 = 0
    pong.switch2 = 0
    pong.switch3 = 0
    pong.switch4 = 0




def beep():
    playsound('sounds/beep.wav', 0)

def cheat_level_up():
    title.lvl = title.lvl + 1

def gameover():
    winsound.PlaySound('sounds\gameover.wav', winsound.SND_ASYNC)
    gonotice.write('Game Over! You have reached LVL {}!'.format(title.lvl),
                   align='center', font=('Courier', 35, 'normal'))
    time.sleep(3)
    title.lvl = 1
    gonotice.clear()
    gonotice.write('\n\n'
                   '                Press Enter to restart\n'
                   '\n'
                   'For finer game music production/pop music production\n'
                   '                whatsapp/wechat 84147172',
                   align='center', font=('Courier', 30, 'normal'))
    ball.velocity = 0
    ball.goto(0,0)
    ball.dx = 0
    ball.dy = 0
    ball_4.goto(0,1000)
    ball_4.dx = 0
    ball_4.dy = 0
    ball_3.dx = 0
    ball_3.dy = 0
    ball_3.goto(0, 1000)
    ball_2.dx = 0
    ball_2.dy = 0
    ball_2.goto(0, 1000)
    pong.switch1 = 0
    pong.switch2 = 0
    pong.switch3 = 0
    pong.switch4 = 0
    paddle_a.goto(-500,0)
    paddle_b.goto(500,0)
    ball.size = 2.0
    pong.bounce_length = 123
    pong.paddle_length = 12
    paddle_a.shape('pics\wood12.gif')
    paddle_b.shape('pics\wood12.gif')



# Key Mapping
pong.listen()
pong.onkeypress(paddle_a_up,'w')
pong.onkeypress(paddle_a_down,'s')
pong.onkeypress(paddle_b_up,'Up')
pong.onkeypress(paddle_b_down,'Down')
pong.onkeypress(restart,'Return')
pong.onkeypress(quitgame,'Escape')
pong.onkeypress(cheat_level_up,'+')

# To handle a window close event

canvas = pong.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", quitgame)


#Main
def main_loop():

    while pong.running == 1:

        time.sleep(0.0035)
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        ball.shapesize(stretch_wid=ball.size, stretch_len=ball.size)
        paddle_a.shapesize(stretch_wid=pong.paddle_length, stretch_len=1)
        paddle_b.shapesize(stretch_wid=pong.paddle_length, stretch_len=1)
        ball_2.shapesize(stretch_wid=ball.size, stretch_len=ball.size)
        ball_3.shapesize(stretch_wid=ball.size, stretch_len=ball.size)
        ball_4.shapesize(stretch_wid=ball.size, stretch_len=ball.size)




        #Bouncing with the screen
        if 360 > ball.ycor() > 350:
            ball.sety(350)
            beep()
            ball.dy = ball.dy * (-1)
        if -360 < ball.ycor() < -350:
            ball.sety(-350)
            beep()
            ball.dy = ball.dy * (-1)





        #Losing the game: GAME AAUWAHHH!
        if 605.6 < ball.xcor()  or  ball.xcor() < -605.6:
            gameover()

        #Bouncing with the paddle
        if 490 < ball.xcor() < 500:
            if paddle_b.ycor() + pong.bounce_length > ball.ycor() > paddle_b.ycor() - pong.bounce_length:
                beep()
                ball.setx(490)
                ball.dx = ball.dx * (-1)
                title.score = title.score + 1
                title.clear()
                title.write('Your Score: {}     Current Level: {}'.format(title.score,title.lvl),
                            align='center', font=('Courier', 30,'normal'))


        if -490 > ball.xcor() > -500:
            if paddle_a.ycor() + pong.bounce_length > ball.ycor() > paddle_a.ycor() - pong.bounce_length:
                beep()
                ball.setx(-490)
                ball.dx = ball.dx * (-1)
                title.score = title.score + 1
                title.clear()
                title.write('Your Score: {}     Current Level: {}'.format(title.score,title.lvl),
                            align='center', font=('Courier', 30,'normal'))






        # Ball_2 Bouncing with the paddle
        if 490 < ball_2.xcor() < 500:
            if paddle_b.ycor() + pong.bounce_length > ball_2.ycor() > paddle_b.ycor() - pong.bounce_length:
                beep()
                ball_2.setx(490)
                ball_2.dx = ball_2.dx * (-1)

        if -490 > ball_2.xcor() > -500:
            if paddle_a.ycor() + pong.bounce_length > ball_2.ycor() > paddle_a.ycor() - pong.bounce_length:
                beep()
                ball_2.setx(-490)
                ball_2.dx = ball_2.dx * (-1)

        # Ball_3 Bouncing with the paddle
        if 490 < ball_3.xcor() < 500:
            if paddle_b.ycor() + pong.bounce_length > ball_3.ycor() > paddle_b.ycor() - pong.bounce_length:
                beep()
                ball_3.setx(490)
                ball_3.dx = ball_3.dx * (-1)

        if -490 > ball_3.xcor() > -500:
            if paddle_a.ycor() + pong.bounce_length > ball_3.ycor() > paddle_a.ycor() - pong.bounce_length:
                beep()
                ball_3.setx(-490)
                ball_3.dx = ball_3.dx * (-1)


        # Ball_4 Bouncing with the paddle
        if 490 < ball_4.xcor() < 500:
            if paddle_b.ycor() + pong.bounce_length > ball_4.ycor() > paddle_b.ycor() - pong.bounce_length:
                beep()
                ball_4.setx(490)
                ball_4.dx = ball_4.dx * (-1)

        if -490 > ball_4.xcor() > -500:
            if paddle_a.ycor() + pong.bounce_length > ball_4.ycor() > paddle_a.ycor() - pong.bounce_length:
                beep()
                ball_4.setx(-490)
                ball_4.dx = ball_4.dx * (-1)

        # On Leveling Up: Single Event
        if title.score == 3:
            title.score = 0
            pong.switch4 = 0
            # Reset all balls speed.
            if ball.dx > 0:
                ball.dx = 2 * ball.velocity
            if ball.dx < 0:
                ball.dx = -2 * ball.velocity
            if ball.dy > 0:
                ball.dy = 2 * ball.velocity
            if ball.dy < 0:
                ball.dy = -2 * ball.velocity
            if ball_2.dx > 0:
                ball_2.dx = 2 * ball.velocity
            if ball_2.dx < 0:
                ball_2.dx = -2 * ball.velocity
            if ball_2.dy > 0:
                ball_2.dy = 1.6 * ball.velocity
            if ball_2.dy < 0:
                ball_2.dy = -1.6 * ball.velocity
            if ball_3.dx > 0:
                ball_3.dx = 2 * ball.velocity
            if ball_3.dx < 0:
                ball_3.dx = -2 * ball.velocity
            if ball_3.dy > 0:
                ball_3.dy = 2.7 * ball.velocity
            if ball_3.dy < 0:
                ball_3.dy = -2.7 * ball.velocity
            if ball_4.dx > 0:
                ball_4.dx = 2 * ball.velocity
            if ball_4.dx < 0:
                ball_4.dx = -2 * ball.velocity
            if ball_4.dy > 0:
                ball_4.dy = 2.7 * ball.velocity
            if ball_4.dy < 0:
                ball_4.dy = -2.7 * ball.velocity

            #Levelup display
            title.lvl = title.lvl + 1
            title.score = 0
            title.clear()
            title.write('Your Score: {}     Current Level: {}'.format(title.score, title.lvl),
                        align='center', font=('Courier', 30, 'normal'))
            gonotice.clear()
            gonotice.write('Congrats! You have leveled up! New features unlocked!',align='center',
                        font=('Courier', 24,'normal'))
            playsound('sounds\lvlup.wav')
            gonotice.clear()


        # Difficulty change for Every Level
        if title.lvl == 2:
            ball.size = 1.6
            pong.bounce_length = 123
            pong.paddle_speed = 40
            ball.velocity = 0.67

        if title.lvl == 3:
            ball.size = 1.4
            ball.velocity = 0.67
            pong.paddle_speed = 45
            if pong.switch1 == 0:
                pong.switch1 = 1
                ball_2.goto(0,0)
                ball_2.dx =  2 * ball.velocity
                ball_2.dy = -1.6 * ball.velocity

        if title.lvl == 4:
            ball.size = 1.2
            pong.paddle_speed = 50
            ball.velocity = 0.67
            pong.paddle_length = 8
            pong.bounce_length = 83
            if pong.switch4 == 0:
                paddle_a.shape('pics\wood8.gif')
                paddle_b.shape('pics\wood8.gif')
                pong.switch4 = 1


        if title.lvl == 5:
            ball.velocity = 0.70
            pong.paddle_length = 6
            pong.bounce_length = 64
            if pong.switch4 == 0:
                paddle_a.shape('pics\wood6.gif')
                paddle_b.shape('pics\wood6.gif')
                pong.switch4 = 1


        if title.lvl > 2:
            ball_2.setx(ball_2.xcor() + ball_2.dx)
            ball_2.sety(ball_2.ycor() + ball_2.dy)
            # Ball_2 Bouncing with the screen
            if 360 > ball_2.ycor() > 350:
                ball_2.sety(350)
                beep()
                ball_2.dy = ball_2.dy * (-1)
            if -360 < ball_2.ycor() < -350:
                ball_2.sety(-350)
                beep()
                ball_2.dy = ball_2.dy * (-1)
            if 605.3 < ball_2.xcor() or ball_2.xcor() < -605.3:
                gameover()


        if title.lvl == 6:
            ball.velocity = 0.74
            if pong.switch2 == 0:
                pong.switch2 = 1
                ball_3.goto(0,0)
                ball_3.dx =   2 * ball.velocity
                ball_3.dy = 2.7 * ball.velocity

        if title.lvl == 7:
            ball.size = 1.15


        if title.lvl > 5:
            ball_3.setx(ball_3.xcor() + ball_3.dx)
            ball_3.sety(ball_3.ycor() + ball_3.dy)
            # ball_3 Bouncing with the screen
            if 360 > ball_3.ycor() > 350:
                ball_3.sety(350)
                beep()
                ball_3.dy = ball_3.dy * (-1)
            if -360 < ball_3.ycor() < -350:
                ball_3.sety(-350)
                beep()
                ball_3.dy = ball_3.dy * (-1)
            if 605.3 < ball_3.xcor() or ball_3.xcor() < -605.3:
                gameover()

        if title.lvl > 6:
            ball.velocity = 0.74 + (title.lvl-6) * 0.04


        if title.lvl == 10:
            if pong.switch3 == 0:
                pong.switch3 = 1
                ball_4.goto(0,0)
                ball_4.dx =   -2 * ball.velocity
                ball_4.dy = -1.63 * ball.velocity


        if title.lvl > 9:
            ball_4.setx(ball_4.xcor() + ball_4.dx)
            ball_4.sety(ball_4.ycor() + ball_4.dy)
            # ball_4 Bouncing with the screen
            if 360 > ball_4.ycor() > 350:
                ball_4.sety(350)
                beep()
                ball_4.dy = ball_4.dy * (-1)
            if -360 < ball_4.ycor() < -350:
                ball_4.sety(-350)
                beep()
                ball_4.dy = ball_4.dy * (-1)
            if 605.3 < ball_4.xcor() or ball_4.xcor() < -605.3:
                gameover()




        pong.update()

try:
    main_loop()
except:
    gonotice.clear()
    gonotice.write(' It seems we have run into some problem. \n This game will be closed.',
                   align='center', font=('Courier', 35, 'normal'))
    time.sleep(3)
    pong.bye()
else:
    pong.bye()