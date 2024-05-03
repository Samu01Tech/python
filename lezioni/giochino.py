import tkinter as tk

STEP = 10

def spostarettangolo(event):
    global RECT_X, RECT_Y, canvas
    if event.keysym == 'Up':
        if RECT_Y > 0:
            RECT_Y -= STEP
    elif event.keysym == 'Down':
        if RECT_Y < 350:
            RECT_Y += STEP
    elif event.keysym == 'Left':
        RECT_X -= STEP
    elif event.keysym == 'Right':
        RECT_X += STEP

    canvas.coords(rectangle, RECT_X, RECT_Y, RECT_X + 50, RECT_Y + 50)


zebra = tk.Tk()
zebra.title("Gioco")
zebra.attributes('-topmost', 1)

canvas = tk.Canvas(zebra, width=400, height=400, bg='skyblue')
canvas.pack()

playerImage = tk.PhotoImage(file="./assets/ghost.gif")
player = canvas.create_image(100, 100, image=playerImage)

# zebra.bind('<Key>', spostarettangolo)

zebra.mainloop()
