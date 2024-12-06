import turtle

class seven_seg(turtle.Turtle):
    def __init__(self,color):
        super().__init__()
        self.speed = 0
        self.tracer = 0
        self.colormode = 255
        self.color = color
        self.penup()
        self.setheading(0)
        self.goto(0, 0)
        self.pensize(10)

    def draw(self,digit):
        if digit == 0:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.right(90)
            self.penup()

        if digit == 1:
            self.goto(50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.forward(100)
            self.left(90)
            self.penup()

        if digit == 2:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.penup()

        if digit == 3:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.forward(-100)
            self.left(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.left(90)
            self.penup()

        if digit == 4:
            self.goto(-50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.forward(-100)
            self.forward(-100)
            self.right(90)
            self.penup()

        if digit == 5:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.forward(-100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.right(90)
            self.forward(100)
            self.left(90)
            self.left(90)
            self.penup()

        if digit == 6:
            self.draw(5)
            self.goto(-50, 0)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.penup()

        if digit == 7:
            self.goto(-50, 100)
            self.pendown()
            self.forward(100)
            self.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            self.goto(-50, 0)
            self.pendown()
            self.forward(100)
            self.penup()

        if digit == 9:
            self.draw(5)
            self.goto(50, 100)
            self.pendown()
            self.right(90)
            self.forward(100)
            self.left(90)
            self.penup()

    def clear(self):
        self._clear()

    def my_delay(self,dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass

# def init(my_turtle, color):
#     turtle.speed(0)
#     turtle.tracer(0)
#     turtle.hideturtle()
#     turtle.colormode(255)
#
#     my_turtle.color(color)
#     my_turtle.penup()
#     my_turtle.setheading(0)
#     my_turtle.goto(0, 0)
#     my_turtle.pensize(10)
#
#
# def draw(my_turtle, digit):
#     if digit == 0:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.penup()
#
#     if digit == 1:
#         my_turtle.goto(50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 2:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.penup()
#
#     if digit == 3:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 4:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.forward(-100)
#         my_turtle.right(90)
#         my_turtle.penup()
#
#     if digit == 5:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 6:
#         draw(my_turtle, 5)
#         my_turtle.goto(-50, 0)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
#     if digit == 7:
#         my_turtle.goto(-50, 100)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.forward(-100)
#         draw(my_turtle, 1)
#
#     if digit == 8:
#         draw(my_turtle, 0)
#         my_turtle.goto(-50, 0)
#         my_turtle.pendown()
#         my_turtle.forward(100)
#         my_turtle.penup()
#
#     if digit == 9:
#         draw(my_turtle, 5)
#         my_turtle.goto(50, 100)
#         my_turtle.pendown()
#         my_turtle.right(90)
#         my_turtle.forward(100)
#         my_turtle.left(90)
#         my_turtle.penup()
#
# def clear(my_turtle):
#     my_turtle.clear()
#
# def my_delay(dt):
#     import time
#     start =  time.time()
#     while time.time() - start < dt:
#         pass
#
tom_color = (255, 0, 0)
Tom = seven_seg(tom_color)
delay_in_seconds = 0.2
while True:
    for i in range(0, 10):
        Tom.clear()
        Tom.draw(i)
        Tom.my_delay(delay_in_seconds)

Tom.done()

