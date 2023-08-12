import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

ball = canvas.create_oval(100, 100, 200, 200)

iteration = 0  # To count the number of iterations

def move_ball():
    global iteration  # Use the global variable

    # Get current coordinates of the ball
    coords = canvas.coords(ball)
    x = coords[0]
    y = coords[1]

    x += 5
    y += 5

    if x >= 490 or x <= 10:
        x -= 5  # Move back if exceeding boundaries
    if y >= 490 or y <= 10:
        y -= 5  # Move back if exceeding boundaries

    canvas.coords(ball, x, y)  # Update ball coordinates

    iteration += 1
    if iteration < 100:  # Stop after 100 iterations
        canvas.after(10, move_ball)


move_ball()

root.mainloop()