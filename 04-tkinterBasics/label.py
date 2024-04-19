import tkinter as tk
from tkinter.messagebox import showinfo

def clicked():
    showinfo(title='Messaggio', message='Hai cliccato il bottone!')

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Giochino')
    window.resizable(False, False)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.attributes('-topmost', 1) # in primo piano

    label = tk.Label(window, text="Un'immagine", font=("Sono una Stringa", 24))
    photo = tk.PhotoImage(file="./assets/logo.png")
    label.config(image=photo, compound='top')
    label.config(justify="left")
    label.pack(expand=True)

    button = tk.Button(window, text="Clicca qui", command=clicked)
    button.pack(expand=True)
  

    window.mainloop()

if __name__ == "__main__":
    main()