import turtle
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('snow')
t=turtle.Turtle()
t_ground=turtle.Turtle()

t.penup()
t.goto(150,200)
t.pendown()
t.write("Merry Christmas", font=("arial", 30, "bold"), align="center")




t_ground.speed(0)
t_ground.pencolor('black')
t_ground.fillcolor('lightblue')

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)


t.pencolor("green")


t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,50)
t.pendown()
t.goto(-40,10)
t.goto(40,10)
t.goto(0,50)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,25)
t.pendown()
t.goto(-60,-25)
t.goto(60,-25)
t.goto(0,25)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.goto(-80,-50)
t.goto(80,-50)
t.goto(0,0)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()



t.pencolor("black")

import turtle

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(10)

t.penup()
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color("red")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()



t.penup()
t.goto(300, -50)
t.pendown()
t.begin_fill()
t.color("red")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()



t.penup()
t.goto(200, -50)
t.pendown()
t.begin_fill()
t.color("red")
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.end_fill()


t.hideturtle()


t_ground.fillcolor('white')
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(-100,-100)
t_ground.pendown()
t_ground.circle(50)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(-100,-5)
t_ground.pendown()
t_ground.circle(35)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(-100,60)
t_ground.pendown()
t_ground.circle(25)
t_ground.end_fill()


t_ground.penup()
t_ground.pencolor('black')
t_ground.fillcolor('black')
t_ground.begin_fill()
t_ground.goto(-90,90)
t_ground.circle(5)
t_ground.end_fill()
t_ground.penup()
t_ground.begin_fill()
t_ground.goto(-110,90)
t_ground.circle(5)
t_ground.end_fill()
t_ground.penup()


t_ground.goto(100,85)
t_ground.pencolor('orange')
t_ground.fillcolor('orange')
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(-85,82)
t_ground.goto(-100,75)
t_ground.goto(-100,85)
t_ground.end_fill()
t_ground.penup()
t_ground.goto(-100,66)




import turtle


t = turtle.Turtle()
t.speed(3)

t.penup()
t.goto(-100, -50)
t.pendown()
t.pensize(5)
t.color("red", "white")
t.setheading(90)
t.circle(50, 180)
t.penup()
t.goto(-100, -50)
t.pendown()
t.setheading(270)
t.forward(100)


turtle.done()


