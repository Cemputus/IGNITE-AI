import tkinter as tk
import winsound  # For sound effects (Windows only)
# import pygame  # Uncomment this line and related code for cross-platform sound support

# Initialize the Tkinter window
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

# Initialize scores
player1_score = 0
player2_score = 0
winning_score = 5  # Set win condition

# Display scores
score_text = canvas.create_text(300, 50, text=f"{player1_score} : {player2_score}", font=("Arial", 24), fill="white")

# Ball movement and speed
ball_dx = 3
ball_dy = 3

def reset_ball():
    """Reset the ball to the center after a point is scored."""
    global ball_dx, ball_dy
    canvas.coords(ball, 290, 190, 310, 210)
    ball_dx = -ball_dx  # Reverse direction
    ball_dy = 3  # Reset ball movement

def play_sound(sound_type):
    """Play a sound effect based on the type."""
    if sound_type == "hit":
        winsound.Beep(1000, 100)  # Example beep sound (change as needed)
    elif sound_type == "score":
        winsound.Beep(800, 200)  # Example beep sound (change as needed)
    # For cross-platform sound effects, use pygame.mixer.music.load() and pygame.mixer.music.play()

def move_ball():
    global ball_dx, ball_dy, player1_score, player2_score
    canvas.move(ball, ball_dx, ball_dy)
    pos = canvas.coords(ball)

    # Bounce off top/bottom walls
    if pos[1] <= 0 or pos[3] >= 400:
        ball_dy = -ball_dy
        play_sound("hit")
    
    # Bounce off paddles
    if pos[0] <= 40 and pos[1] >= canvas.coords(left_paddle)[1] and pos[3] <= canvas.coords(left_paddle)[3]:
        ball_dx = -ball_dx
        play_sound("hit")
    elif pos[2] >= 560 and pos[1] >= canvas.coords(right_paddle)[1] and pos[3] <= canvas.coords(right_paddle)[3]:
        ball_dx = -ball_dx
        play_sound("hit")

    # Scoring system
    if pos[0] <= 0:  # Player 2 scores
        player2_score += 1
        update_score()
        play_sound("score")
        if player2_score >= winning_score:
            end_game("Player 2 Wins!")
        else:
            reset_ball()
    elif pos[2] >= 600:  # Player 1 scores
        player1_score += 1
        update_score()
        play_sound("score")
        if player1_score >= winning_score:
            end_game("Player 1 Wins!")
        else:
            reset_ball()

    # Game loop
    root.after(20, move_ball)

def update_score():
    """Update the displayed score."""
    canvas.itemconfig(score_text, text=f"{player1_score} : {player2_score}")

def end_game(message):
    """Display a winner message and stop the game."""
    canvas.create_text(300, 200, text=message, font=("Arial", 36), fill="white")
    root.after(2000, root.quit)  # Close the game after 2 seconds

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
