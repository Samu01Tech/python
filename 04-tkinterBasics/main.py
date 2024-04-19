import tkinter as tk

# write a full tkinter application where the an image can move around the screen with the arrow keys

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Giochino')
    window.resizable(False, False)
    window.attributes('-topmost', 1) # in primo piano

    # center the window to the screen
    screenX = window.winfo_screenwidth()
    screenY = window.winfo_screenheight()
    moveByX = int(screenX / 2 - WIDTH / 2)
    moveByY = int(screenY / 2 - HEIGHT / 2)
    window.geometry(f"{WIDTH}x{HEIGHT}+{moveByX}+{moveByY}")

    # create a label with an image
    player = tk.Label(window)
    photo = tk.PhotoImage(file="./assets/logo.png")
    player.config(image=photo)
    player.pack(expand=True)

    # bind the arrow keys to move the image
    def move(e):
        if e.keysym == 'Up':
            # chek if the label is in the window
            if player.winfo_y() - 5 < 0:
                player.place(x=player.winfo_x(), y=0)
            else:
                player.place(x=player.winfo_x(), y=player.winfo_y() - 5)
        elif e.keysym == 'Down':
            if player.winfo_y() + 5 > HEIGHT - 50:
                player.place(x=player.winfo_x(), y=HEIGHT - 50)
            else:
                player.place(x=player.winfo_x(), y=player.winfo_y() + 5)
        elif e.keysym == 'Left':
            if player.winfo_x() - 5 < 0:
                player.place(x=0, y=player.winfo_y())
            else:
                player.place(x=player.winfo_x() - 5, y=player.winfo_y())
        elif e.keysym == 'Right':
            if player.winfo_x() + 5 > WIDTH - 50:
                player.place(x=WIDTH - 50, y=player.winfo_y())
            else:
                player.place(x=player.winfo_x() + 5, y=player.winfo_y())
    
    window.bind('<Up>', move)
    window.bind('<Down>', move)
    window.bind('<Left>', move)
    window.bind('<Right>', move)

    window.mainloop()

if __name__ == "__main__":
    main()