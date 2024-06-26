from turtle import Turtle




class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.Y_MOVEMENT = 10
        self.X_MOVEMENT = 10
        self.move_speed = 0.1
        self.penup()
        self.goto(0,0)


    

    def move(self):
        new_x = self.xcor()+self.X_MOVEMENT
        new_y = self.ycor()+self.Y_MOVEMENT
        self.goto(new_x, new_y)
 
    def bounce_y(self):
        self.Y_MOVEMENT *=-1

    def  bounce_x(self):
        self.X_MOVEMENT *=-1  
        self.move_speed*=0.9

    def increase_speed(self):
        self.X_MOVEMENT *= 1.1
        self.Y_MOVEMENT *= 1.1    
    
    

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()         