import turtle as t

# ===== Screen setup =====
screen = t.Screen()
screen.setup(800, 800)
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

pen_point(-100, 100, 0)
draw_snow(100, min_len=6)

pen_point(-200, 100, 30)  # 각도 바꿔도 안정
draw_snow(100, min_len=6)

t.done()