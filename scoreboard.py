from turtle import Turtle



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.live = 5
        self.scoreboard()
        
        
    def scoreboard(self):
        self.clear()
        self.goto(-255, 260)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))
        self.goto(260, 260)
        self.write(f"Live : {self.live}", align="center", font=("Arial", 15, "normal"))   
        
    
    def increase_score(self):
        self.score += 1
        self.scoreboard()
        
    def decrease_live(self):
        self.live -= 1
        self.scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=("Arial", 30, "normal"))