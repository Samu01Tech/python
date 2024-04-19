import tkinter as tk

def ciao(e):
    print('Ciao')

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Giochino')
    window.resizable(False, False)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.attributes('-topmost', 1) # in primo piano

    text = tk.Label(window, text="Premi Spazio per salutare").pack(expand=True)
    text2 = tk.Label(window, text="Premi Ctrl+V per incollare").pack(expand=True)
    text3 = tk.Label(window, text="Premi Esc per uscire").pack(expand=True)

    window.bind('<space>', ciao)
    window.bind('<Control-v> ', lambda x: print('Incolla!'))
    window.bind('<Escape>', lambda x: window.quit())

    window.mainloop()

if __name__ == "__main__":
    main()