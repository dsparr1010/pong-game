import turtle

window = turtle.Screen()
window.title("Pong Game Tutorial")
window.bgcolor("black")
window.setup(width=800, height=600)
# stops window from updating -- makes game faster
window.tracer(0)


# Score Card
score_a = 0
score_b = 0


# Paddle A
# lower case is module, upper is Class
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid = 5, stretch_len = 1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid = 5, stretch_len = 1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.xSpeed = 1
ball.ySpeed = -1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Bind to keyboard inputs
window.listen()
window.onkeypress(paddleAUp, 'w')
window.onkeypress(paddleADown, 's')
window.onkeypress(paddleBUp, 'Up')
window.onkeypress(paddleBDown, 'Down')

# Main game loop -- window persists
while True:
    window.update()
    # While window is up, move the ball
    ball.setx(ball.xcor() + ball.xSpeed)
    ball.sety(ball.ycor() + ball.ySpeed)

    # Border the ball -- must compare ball's x and y coordinate
    if ball.ycor() > 290:
        ball.sety(209)
        ball.ySpeed *= -1
        
    if ball.ycor() < -290:
        ball.sety(-209)
        ball.ySpeed *= -1

    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.xSpeed *= -1

    if ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.xSpeed *= -1


    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        #ball.setx(340)
        ball.xSpeed *= -1

    if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        #ball.setx(-340)
        ball.xSpeed *= -1
