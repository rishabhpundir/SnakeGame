from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for position in START:
            self.add_segment(position)
    

    def add_segment(self, position):
            new_segment = Turtle(shape="square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.snake_body.append(new_segment)
        

    def extend(self):
        self.add_segment(self.snake_body[-1].position())



    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg - 1].xcor()
            new_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(new_x, new_y)
        self.head.forward(20)

        
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!= LEFT:  
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:  
            self.head.setheading(LEFT)



        
