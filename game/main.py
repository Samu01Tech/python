import tkinter as tk

CANVAS_WIDTH = 480
CANVAS_HEIGHT = 480
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
STEP = 8
GIF_PATH = "./immagini/ghost.gif"


def run_gif(canvas, image, photo_images, interval=250):
    index = 0
    def update_image():
        nonlocal index
        canvas.itemconfig(image, image=photo_images[index])
        # Switch index and schedule next update
        index = (index + 1) % len(photo_images)
        canvas.after(interval, update_image)
    # Start the image switching loop
    update_image()


def move_player(event):
    if event.keysym == 'Left':
        if canvas.coords(player)[0] - PLAYER_WIDTH / 2 > 0:
            canvas.move(player, -STEP, 0)
    elif event.keysym == 'Right':
        if canvas.coords(player)[0] + PLAYER_WIDTH / 2 < CANVAS_WIDTH:
            canvas.move(player, STEP, 0)
    elif event.keysym == 'Up':
        if canvas.coords(player)[1] - PLAYER_HEIGHT / 2 > 0:
            canvas.move(player, 0, -STEP)
    elif event.keysym == 'Down':
        if canvas.coords(player)[1] + PLAYER_HEIGHT / 2 < CANVAS_HEIGHT:
            canvas.move(player, 0, STEP)


window = tk.Tk()
window.title("Gioco")

canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#1E1E1E")
canvas.pack()

playerPicture1 = tk.PhotoImage(file=GIF_PATH, format="gif -index 0", width=PLAYER_WIDTH, height=PLAYER_HEIGHT)

playerPicture2 = tk.PhotoImage(file=GIF_PATH, format="gif -index 1", width=PLAYER_WIDTH, height=PLAYER_HEIGHT)

playerPictures = [playerPicture1, playerPicture2]

player = canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=playerPicture1)

run_gif(canvas, player, playerPictures)
window.bind('<Key>', move_player)

window.mainloop()
