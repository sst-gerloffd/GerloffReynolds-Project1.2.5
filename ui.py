'''
To Do:
- Add upgrades functionality
- Add Total Albert & Current Albert score displays

'''
import turtle

def initialize_ui(screen, font, current_alberts):
    current_score_drawer = turtle.Turtle()
    current_score_drawer.penup()
    current_score_drawer.hideturtle()
    current_score_drawer.goto(200, 200)
    current_score_drawer.write(f"Score: 0", align="center", font=font)
    screen.update()
