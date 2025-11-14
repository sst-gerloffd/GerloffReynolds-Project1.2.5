# === imports === #
import turtle as turt

# === initalize constants/lists === #
screen = turt.Screen()
APC = 1
TA = 0
CA = 0
APS = 0
font = ("roboto", 18, "bold")

# === Turtle Initialization === #
# - score display turtle - #
al_score = turt.Turtle()
al_score.penup()
al_score.hideturtle()
al_score.goto(200,200)
al_score.write(f"Score: {CA}", align="center", font=font)
# - upgrades - #
upgrades = []
for _ in range(12):
    upgrade = turt.Turtle()
    upgrade.penup()
    upgrades.append(upgrade)

# === Game Functions === #
def click(x,y):
    global TA, APC, CA
    TA += APC
    CA += APC
    al_score.clear()
    al_score.write(f"Score: {CA}", align="center", font=font)
    screen.update()
    
# === Run Game === #
screen.onscreenclick(click)


screen.mainloop()
