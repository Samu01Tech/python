import tkinter as tk
from tkinter.messagebox import showinfo

def logIn(email, password):
    msg = f'You entered email: {email} and password: {password}'
    showinfo(
        title='Information',
        message=msg
    )

def main():
    WIDTH = 400
    HEIGHT = 400

    window = tk.Tk()
    window.title('Sign In')
    window.resizable(False, False)
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.attributes('-topmost', 1) # in primo piano

    email = tk.StringVar()
    password = tk.StringVar()   

    emailLabel = tk.Label(window, text="Email").pack()
    emailEntry = tk.Entry(window, textvariable=email).pack()

    passwordLabel = tk.Label(window, text="Password").pack()
    passwordEntry = tk.Entry(window, textvariable=password,show='*').pack()

    button = tk.Button(window, text="Login", command=lambda: logIn(email.get(), password.get())).pack()

    window.mainloop()

if __name__ == "__main__":
    main()