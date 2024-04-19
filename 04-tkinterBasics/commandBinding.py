import tkinter as tk

def ciao():
    print('Ciao')

def scriviCose(qualcosa):
    print(qualcosa)

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Giochino')
    window.resizable(False, False)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.attributes('-topmost', 1) # in primo piano

    button = tk.Button(window, text="Scrivi Ciao", command=ciao).pack()

    button2 = tk.Button(window, text="Scrivi Hello World! con parametri", command=lambda: scriviCose("Hello World!")).pack()

    window.mainloop()

if __name__ == "__main__":
    main()