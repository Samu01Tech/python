import tkinter as tk

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Giochino')
    window.resizable(False, False)
    window.attributes('-topmost', 1) # in primo piano

    message = tk.Label(window, text="Hello, World!").pack(expand=True)

    # center the window to the screen
    screenX = window.winfo_screenwidth()
    screenY = window.winfo_screenheight()
    moveByX = int(screenX / 2 - WIDTH / 2)
    moveByY = int(screenY / 2 - HEIGHT / 2)
    window.geometry(f"{WIDTH}x{HEIGHT}+{moveByX}+{moveByY}")

    window.mainloop()


if __name__ == "__main__":
    main()