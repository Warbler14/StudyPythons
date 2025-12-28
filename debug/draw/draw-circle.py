import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen = turtle.Screen()
screen.setup(800, 800)
screen.setworldcoordinates(-300, -300, 300, 300)

# turtle.tracer(0, 0)   # 🔥 핵심 가속

# ===== 설정 =====
BIG_R = 220      # 큰 원 반지름
SMALL_R = 20     # 작은 원 반지름
COUNT = 36       # 작은 원 개수 (10도 간격)

# ===== Helpers =====
def pen_point(x, y):
    """Move to (x,y) without drawing and set absolute heading."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# ===== 작은 원들을 원형으로 배치 =====
for i in range(COUNT):
    angle = 2 * math.pi * i / COUNT   # 라디안
    cx = BIG_R * math.cos(angle)
    cy = BIG_R * math.sin(angle)

    # turtle 보정 (중심 → 아래쪽 접점)
    pen_point(cx, cy - SMALL_R)
    t.circle(SMALL_R)

turtle.done()