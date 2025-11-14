# === imports === #
import turtle
import clicker
import ui

# === setup === #

screen = turtle.Screen()
alberts_per_click = 1
total_alberts = 0
current_alberts = 0
alberts_per_second = 0
current_score_font = ("roboto", 18, "bold")

# Initialize UI
ui.initialize_ui(screen, current_score_font, current_alberts)

# === Run Game === #
def handle_click(x, y):
    current_alberts = clicker.click(x, y, current_alberts, total_alberts)
    ui.current_score_drawer.clear()
    ui.current_score_drawer.write(f"Score: {current_alberts}", align="center", font=current_score_font)

screen.onscreenclick(handle_click)
turtle.done()
