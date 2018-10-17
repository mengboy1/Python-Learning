# Turtle绘图
import turtle 

# Generate Turtle object 
t = turtle.Turtle()

# Set the pen
t.pensize(2)
t.pencolor('black')
t.speed(3)	# 范围[0,10]整数

# Draw a square
t.penup()	# 提起笔移动
t.goto(-50, -50)
t.pendown()	# 放下笔绘制
for i in range(4):
	t.forward(100)
	t.left(90)	

# Move to the center of this square
t.penup()
t.goto(0, 0)
t.pendown()

# Draw the demo in the documentation
t.color('red', 'yellow')
t.hideturtle()
t.begin_fill()
while True:
	t.forward(200)
	t.left(170)
	if abs(t.pos()) < 1:
		break
t.end_fill()

# Pause the program
print('Press Enter to continue...')
input()

