
class InitialBoard():
    def __init__(self):
        def draw_inital_bricks(PADDLE_WIDTH, PADDLE_HEIGHT):
            # hardcoding the bricks
            set_of_bricks = set()
            brick1 = Brick(0, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick2 = Brick(80, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick3 = Brick(160, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick4 = Brick(240, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick5 = Brick(320, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick6 = Brick(0, 20, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick7 = Brick(80, 20, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick8 = Brick(160, 20, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick9 = Brick(240, 20, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick10 = Brick(320, 20, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick11 = Brick(0, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick12 = Brick(80, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick13 = Brick(160, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick14 = Brick(240, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
            brick15 = Brick(320, 40, PADDLE_WIDTH, PADDLE_HEIGHT)
            set_of_bricks.add(brick1)
            set_of_bricks.add(brick2)
            set_of_bricks.add(brick3)
            set_of_bricks.add(brick4)
            set_of_bricks.add(brick5)
            set_of_bricks.add(brick6)
            set_of_bricks.add(brick7)
            set_of_bricks.add(brick8)
            set_of_bricks.add(brick9)
            set_of_bricks.add(brick10)
            set_of_bricks.add(brick11)
            set_of_bricks.add(brick12)
            set_of_bricks.add(brick13)
            set_of_bricks.add(brick14)
            set_of_bricks.add(brick15)
            return set_of_bricks

        def drawPaddleAndBall():
            # draw paddle and ball in initial positions
            draw_rectangle(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            draw_circle(ball_x, ball_y, ball_radius)