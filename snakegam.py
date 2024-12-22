# this is snake


import turtle # used turtle library instead of pygame
import time
import random # import for random food placement

#initial delay
delay = 0.1

# score code
score = 0
high_score = 0

# screen setup
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("blue") #blue background
wn.setup(width=600, height=600) #600x600 frame
wn.tracer(0) #t urns off automatic screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food code
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

#array for snake segments
segments = []

# pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# sname movement code
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# functions for moving snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# wasd controls 
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# main game loop
while True:
    wn.update()

    # check for collision w border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide segments 
        for segment in segments:
            segment.goto(1000, 1000)
        
        # clear segments list n reset score n delay n pen
        segments.clear()
        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # check for collision with food
    if head.distance(food) < 20:
        # move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)


        # add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)


        # shorten delay
        delay -= 0.001

        # increase score n update high score
        score += 10
        if score > high_score:
            high_score = score
        
        # write score and high score + formatting
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # move end segments first in opposite order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)


    # move segment 0 (first) to same place as head
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()    

    # checkfor head collision w self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear() #clear segments list
            score = 0  # reset score
            delay = 0.1 # reset delay

            # update scores display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

wn.mainloop()