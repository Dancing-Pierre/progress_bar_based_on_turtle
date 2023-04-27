import turtle


def draw_progress_bar(width, height, percent):
    t = turtle.Turtle()

    turtle.bgcolor("white")

    t.width(height)

    t.color("blue")

    progress = (percent / 100) * width

    t.penup()
    t.goto(-width / 2, height * 2)
    t.pendown()

    t.forward(progress)

    t.color("gray")
    t.forward(width - progress)

    t.penup()
    t.goto(0, height * 3)
    t.pendown()

    t.pencolor("white")
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(50)

    t.pencolor("black")
    t.write(str(percent) + "%", align="center", font=("Arial", 12, "normal"))

    t.hideturtle()

    turtle.update()


for i in range(1, 101):
    draw_progress_bar(300, 20, i)
    if i == 100:
        break
