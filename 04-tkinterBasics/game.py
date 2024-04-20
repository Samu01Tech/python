import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PLAYER_SIZE = 32
STEP = 10

# window setup
window = tk.Tk()
window.title('Gioco')
window.resizable(False, False)
window.attributes('-topmost', 1)

# game canvas
canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

# player
playerImage = tk.PhotoImage(file="./assets/sprite.png").subsample(4,4)
playerImage.configure(width=PLAYER_SIZE, height=PLAYER_SIZE)
player = canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=playerImage)
# player = canvas.create_rectangle(
#     (CANVAS_WIDTH - PLAYER_SIZE) / 2, 
#     (CANVAS_HEIGHT - PLAYER_SIZE) / 2, 
#     (CANVAS_WIDTH + PLAYER_SIZE) / 2, 
#     (CANVAS_HEIGHT + PLAYER_SIZE) / 2, 
#     fill='red')

# def move(e):
#     print(e.keysym)
#     print("Old positions" + str(canvas.coords(player)))
#     if e.keysym == 'Up':
#         if canvas.coords(player)[1] - STEP < 0:
#             return
#         canvas.move(player, 0, -STEP)
#     elif e.keysym == 'Down':
#         if canvas.coords(player)[3] + STEP > CANVAS_HEIGHT:
#             return
#         canvas.move(player, 0, STEP)
#     elif e.keysym == 'Left':
#         if canvas.coords(player)[0] - STEP < 0:
#             return
#         canvas.move(player, -STEP, 0)
#     elif e.keysym == 'Right':
#         if canvas.coords(player)[2] + STEP > CANVAS_WIDTH:
#             return
#         canvas.move(player, STEP, 0)
#     print("New Positions" + str(canvas.coords(player)))

def move(e):
    print(e.keysym)
    if(e.keysym == 'Up'):
        if canvas.coords(player)[1] - PLAYER_SIZE/2 - STEP < 0:
            return
        canvas.move(player, 0, -STEP)
    elif(e.keysym == 'Down'):
        if canvas.coords(player)[1] + PLAYER_SIZE/2 + STEP > CANVAS_HEIGHT:
            return
        canvas.move(player, 0, STEP)
    elif(e.keysym == 'Left'):
        if canvas.coords(player)[0] - PLAYER_SIZE/2 - STEP < 0:
            return
        canvas.move(player, -STEP, 0)
    elif(e.keysym == 'Right'):
        if canvas.coords(player)[0] + PLAYER_SIZE/2 + STEP > CANVAS_WIDTH:
            return
        canvas.move(player, STEP, 0)
    print(canvas.coords(player))

window.bind('<Up>', lambda e: move(e))
window.bind('<Down>', lambda e: move(e))
window.bind('<Left>', lambda e: move(e))
window.bind('<Right>', lambda e: move(e))

window.bind('<Escape>', lambda e: window.quit())

window.mainloop()