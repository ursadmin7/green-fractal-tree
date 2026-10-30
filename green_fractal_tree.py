
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Green Fractal Tree - Upward and Downward")

tree = turtle.Turtle()
tree.speed(0)
tree.color("green")
tree.pensize(2)

screen.tracer(0, 0)

start_time = time.time()
TIME_LIMIT = 15


def draw_tree(branch, direction):
    if branch < 5 or time.time() - start_time >= TIME_LIMIT:
        return

    tree.forward(branch)
    screen.update()

    tree.right(direction * 25)
    draw_tree(branch * 0.75, direction)

    tree.left(direction * 50)
    draw_tree(branch * 0.75, direction)

    tree.right(direction * 25)
    tree.backward(branch)
    screen.update()


# Grow the tree upwards
tree.penup()
tree.goto(0, -250)
tree.setheading(90)
tree.pendown()

draw_tree(100, 1)

# Grow the tree downwards
tree.penup()
tree.goto(0, 250)
tree.setheading(270)
tree.pendown()

draw_tree(100, -1)

screen.update()
turtle.done()