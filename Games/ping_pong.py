import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Ping Pong Game")

# Create canvas
canvas = tk.Canvas(root, width=600, height=400, bg='black')
canvas.pack()

# Create ball
ball = canvas.create_oval(290, 190, 310, 210, fill="white")

# Create paddles
left_paddle = canvas.create_rectangle(30, 150, 40, 250, fill="blue")
right_paddle = canvas.create_rectangle(560, 150, 570, 250, fill="red")

# Ball movement and speed
ball_dx = 3
ball_dy = 3

def move_ball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    pos = canvas.coords(ball)

    # Bounce off top/bottom walls
    if pos[1] <= 0 or pos[3] >= 400:
        ball_dy = -ball_dy
    
    # Bounce off paddles
    if pos[0] <= 40 and pos[1] >= canvas.coords(left_paddle)[1] and pos[3] <= canvas.coords(left_paddle)[3]:
        ball_dx = -ball_dx
    if pos[2] >= 560 and pos[1] >= canvas.coords(right_paddle)[1] and pos[3] <= canvas.coords(right_paddle)[3]:
        ball_dx = -ball_dx

    # Game loop
    root.after(20, move_ball)

# Paddle movement
def move_left_paddle(event):
    if event.keysym == 'w':
        canvas.move(left_paddle, 0, -20)
    elif event.keysym == 's':
        canvas.move(left_paddle, 0, 20)

def move_right_paddle(event):
    if event.keysym == 'Up':
        canvas.move(right_paddle, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(right_paddle, 0, 20)

# Bind keys to paddle movement
root.bind('<KeyPress-w>', move_left_paddle)
root.bind('<KeyPress-s>', move_left_paddle)
root.bind('<KeyPress-Up>', move_right_paddle)
root.bind('<KeyPress-Down>', move_right_paddle)

# Start game
move_ball()
root.mainloop()
