#Alex Chan
#June 18, 2016
#Breakout Version 1, for fun using cs1lib, modeled after breakout game from Stanford and cs1 pong lab
from cs1lib import *
from time import sleep
from Brick import *
from random import randint
from random import randrange
counter = 0
def check_if_lines_collide(hx1,hx2,hy,vy1,vy2,vx):
    return (hy > vy1 and hy < vy2) and (vx > hx1 and vx < hx2)

def main():
    enable_smoothing()
    WINDOW_SIZE = 400
    WINDOW_CENTER = WINDOW_SIZE / 2
    paddle_x = 160
    paddle_y = 380
    PADDLE_WIDTH = 80
    PADDLE_HEIGHT = 20
    PADDLE_SHIFT = 8
    ball_x = WINDOW_CENTER
    ball_y = WINDOW_CENTER
    ball_radius = 10
    ball_shift_h = 0                #how many pixels the ball will shift horizontally
    ball_shift_v = 0                #how many pixels the ball will shift vertically


    #hardcoding the bricks
    list_of_bricks = []
    brick1 = Brick(0,0,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick2 = Brick(80,0,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick3 = Brick(160,0,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick4 = Brick(240,0,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick5 = Brick(320,0,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick6 = Brick(0,20,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick7 = Brick(80,20,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick8 = Brick(160,20,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick9 = Brick(240,20,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick10 = Brick(320,20,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick11 = Brick(0,40,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick12 = Brick(80,40,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick13 = Brick(160,40,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick14 = Brick(240,40,PADDLE_WIDTH,PADDLE_HEIGHT)
    brick15 = Brick(320,40,PADDLE_WIDTH,PADDLE_HEIGHT)
    list_of_bricks.append(brick1)
    list_of_bricks.append(brick2)
    list_of_bricks.append(brick3)
    list_of_bricks.append(brick4)
    list_of_bricks.append(brick5)
    list_of_bricks.append(brick6)
    list_of_bricks.append(brick7)
    list_of_bricks.append(brick8)
    list_of_bricks.append(brick9)
    list_of_bricks.append(brick10)
    list_of_bricks.append(brick11)
    list_of_bricks.append(brick12)
    list_of_bricks.append(brick13)
    list_of_bricks.append(brick14)
    list_of_bricks.append(brick15)

    counter = 0 #counter to speed up ball if necessary

    #drawing everything
    while not window_closed():
        clear()
        enable_smoothing()
        enable_stroke()

        #loop through bricks and draw em
        for brick in list_of_bricks:
            set_fill_color(1,0,0)   #color everything red
            brick.draw()
            if check_if_lines_collide(brick.get_x(), brick.get_x() + brick.get_width(), brick.get_y() + brick.get_height(), ball_y - ball_radius, ball_y + ball_radius, ball_x):
                brick.delete()
                brick.alive = False
                counter += 1
                print 'ball hit brick'
                ball_shift_v = - ball_shift_v
                ball_shift_v += 1
                print 'ball speed is' + str(ball_shift_v)

        #quit the game by pressing q
        if is_key_pressed("q"):
            cs1_quit()

        #draw paddle and ball in initial positions
        draw_rectangle(paddle_x,paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT)
        draw_circle(ball_x,ball_y,ball_radius)

        #movement of paddle to the left and right
        if is_key_pressed("m") and paddle_x + 80 <= WINDOW_SIZE:
            paddle_x = paddle_x + PADDLE_SHIFT
        if is_key_pressed("z") and paddle_x >= 0:
            paddle_x = paddle_x - PADDLE_SHIFT

        #returning the ball to the center of the screen
        if is_key_pressed(" "):
            for brick in list_of_bricks:
                brick.reset()
            counter = 0
            ball_x = WINDOW_CENTER
            ball_y = WINDOW_CENTER
            ball_shift_v = 2.5
            ball_shift_h = 2.5

        #Colision detection
        #if ball connects with right wall
        if check_if_lines_collide(ball_x - ball_radius, ball_x + ball_radius, ball_y, 0, 400, WINDOW_SIZE - ball_radius):
            print 'ball hit right wall'
            ball_shift_h = - ball_shift_h

        #if ball connects with left wall
        if check_if_lines_collide(ball_x - ball_radius, ball_x + ball_radius, ball_y, 0, 400, 0):
            print('ball hit left wall')
            ball_shift_h = - ball_shift_h

        #if ball hits paddle
        if check_if_lines_collide(paddle_x, paddle_x + PADDLE_WIDTH, paddle_y, ball_y - ball_radius, ball_y + ball_radius, ball_x):
            ball_shift_v = - ball_shift_v
            ball_y = ball_y - 3
            print 'ball hit paddle'
            counter += 1
            if counter % 5 == 0:
                ball_shift_v += 1

        #if ball hits top wall
        if check_if_lines_collide(0, WINDOW_SIZE, 0, ball_y - ball_radius, ball_y + ball_radius, ball_x):
            ball_shift_v = - ball_shift_v


        #redrawing the state of the game
        ball_x = ball_x + ball_shift_h
        ball_y = ball_y + ball_shift_v
        draw_rectangle(paddle_x,paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT)
        draw_circle(ball_x,ball_y,ball_radius)
        request_redraw()
        sleep(.015)




start_graphics(main)