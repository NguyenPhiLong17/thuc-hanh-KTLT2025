import turtle
import random

# Tạo đối tượng vẽ
painter = turtle.Turtle()
painter.speed(0)
painter.pensize(3)

colors = ["red", "blue", "green", "orange", "purple", "cyan"]

# Vẽ 12 vòng tròn
for i in range(12):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)   # Xoay 30 độ để được 12 hướng

# Giữ màn hình
turtle.done()
