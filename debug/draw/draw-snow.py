import turtle as t
import random
from collections import namedtuple

# ===== Screen setup =====
width = 800
height = 800
screen = t.Screen()
screen.setup(width, height)
screen.setworldcoordinates(-300, -300, 300, 300)

# ===== Helpers =====
def pen_point(x, y, angle=0):
    """Move to (x,y) without drawing and set absolute heading."""
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

def snow_line(length, min_len=10):
    """Draw a Koch curve segment of given length."""
    if length <= min_len:
        t.forward(length)
        return

    new_len = length / 3.0
    snow_line(new_len, min_len)
    t.left(60)
    snow_line(new_len, min_len)
    t.right(120)
    snow_line(new_len, min_len)
    t.left(60)
    snow_line(new_len, min_len)

def draw_snow(size, min_len=10):
    """Draw Koch snowflake (3 Koch curves). Preserves turtle heading."""
    start_heading = t.heading()

    for _ in range(3):
        snow_line(size, min_len)
        t.right(120)

    t.setheading(start_heading)  # restore

# ===== Main =====
t.speed(0)
t.hideturtle()

Point = namedtuple('Point', ['x', 'y'])
world_map = {}

for i in range(20):
    while True:
        rand_x = random.randint(1, 300)
        rand_y = random.randint(1, 300)
        new_pos = Point(x=rand_x, y=rand_y)

        key = f"entity_{rand_x}_{rand_y}"

        if len(world_map) == 0:
            world_map[key] = new_pos
            break

        if new_pos not in world_map.values():
            world_map[key] = new_pos
            break  # Success! Exit the 'while' loop
        else:
            print(f"Collision at {new_pos}! Recalculating...")

print(world_map)

for name, pos in world_map.items():
    print(name, pos)

    pen_point(-pos.x, pos.y, 0)
    draw_snow(100, min_len=6)

t.done()