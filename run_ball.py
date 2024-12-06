import turtle
from ball import Ball
import random

canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
print(canvas_width, canvas_height)
xpos = []
ypos = []
vx = []
vy = []
ball_color = []


class MoreBall(Ball):
    def __init__(self):
        super().__init__(size, x, y, vx, vy, color)
        self.num_balls = 5
        self.speed = 0
        self.tracer = 0
        self.hideturtle()
        self.ball_radius = 0.05 * canvas_width
        self.colormode = 255
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

    def random_ball(self):
        for _ in range(self.num_balls):
            self.xpos.append(random.uniform(-1*canvas_width + self.ball_radius, canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*canvas_height + self.ball_radius, canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # self.draw_ball(ball_color[i], bally.ball_radius, xpos[i], ypos[i])

    def draw_border(self):
        self.penup()
        self.goto(-canvas_width, -canvas_height)
        self.pensize(10)
        self.pendown()
        self.color((0, 0, 0))
        for _ in range(2):
            self.forward(2*canvas_width)
            self.left(90)
            self.forward(2*canvas_height)
            self.left(90)


dt = 0.2  # time step
bally = MoreBall()
bally.clear()
bally.draw_border()
for i in range(bally.num_balls):
    bally.random_ball()
    bally.move_ball(i, xpos, ypos, vx, vy, dt)
    bally.update_ball_velocity(i, xpos, ypos, vx, vy, canvas_width, canvas_height, bally.ball_radius)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
