import turtle

def bubble(t,n,r):
	if n == 0:
		return

	radius_child = r // 2
	distance_child = r + radius_child
	
	t.down()
	t.circle(r)
	t.up()

	t.left(90)
	t.forward(radius_child)
	t.right(90)
	t.forward(distance_child)
	
	first_child = bubble(t,n-1,radius_child)
	
	t.backward(distance_child)
	t.left(90)
	t.backward(radius_child)
	t.right(90)
	
	t.right(90)
	t.forward(radius_child*2)
	t.left(90)

	second_child = bubble(t,n-1,radius_child)
	
	t.right(90)
	t.backward(radius_child*2)
	t.left(90)

	return

def main():
	t = turtle.Turtle()
	t.speed('slowest')
	bubble(t,4,60)
	turtle.Screen().exitonclick()

main()
