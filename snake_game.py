import random
import turtle
import time

delay = 0.15

window = turtle.Screen()
window.title('Snake_Game')
window.bgcolor('green')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.80, 0.80)
food.goto(0, 0)

tails = []
score = 0

record = turtle.Turtle()
record.speed(0)
record.shape("square")
record.color("white")
record.penup()
record.hideturtle()
record.goto(0, 260)
record.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

while True:
    window.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for tail in tails:
            tail.goto(1000, 1000)
        tails = []
        score = 0
        delay = 0.1

        record.clear()
        record.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("white")
        new_tail.penup()
        tails.append(new_tail)

        delay -= 0.001

        score = score + 10
        record.clear()
        record.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()

    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            puan = 0
            record.clear()
            record.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15

    time.sleep(delay)
