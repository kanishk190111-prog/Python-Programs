import turtle


def draw_petal(t, size):
    """Draws a single petal using two arcs."""
    for _ in range(2):
        t.circle(size, 60) 
        t.left(120)  


def create_artwork():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Colourful Loop Artwork")

    t = turtle.Turtle()
    t.speed(0)  
    t.width(2)
    turtle.colormode(255)  

    colors = [
        (255, 0, 127), 
        (0, 255, 255), 
        (255, 215, 0), 
        (138, 43, 226), 
        (255, 69, 0),  
        (50, 205, 50), 
    ]

    num_petals = 36  
    angle = 360 / num_petals

    for i in range(num_petals):
        color = colors[i % len(colors)]
        t.pencolor(color)
        t.fillcolor(color)

        t.begin_fill()
        draw_petal(t, 150)
        t.end_fill()

        t.left(angle)  

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    create_artwork()