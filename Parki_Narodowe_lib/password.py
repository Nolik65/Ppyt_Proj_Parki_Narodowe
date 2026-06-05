from tkinter import *
from tkinter import messagebox


def login_window() -> bool:
    poprawny_login = "admin"
    poprawne_haslo = "1234"

    zalogowano = False

    def sprawdz_logowanie():
        nonlocal zalogowano

        login = entry_login.get()
        haslo = entry_haslo.get()

        if login == poprawny_login and haslo == poprawne_haslo:
            zalogowano = True
            root_login.destroy()
        else:
            messagebox.showerror("Błąd logowania", "Niepoprawny login lub hasło")
            entry_haslo.delete(0, END)
            entry_haslo.focus()

    root_login = Tk()
    root_login.title("Logowanie")
    root_login.geometry("300x180")

    label_tytul = Label(root_login, text="Witaj, wprowadź login i hasło")
    label_login = Label(root_login, text="Login:")
    label_haslo = Label(root_login, text="Hasło:")

    entry_login = Entry(root_login)
    entry_haslo = Entry(root_login, show="+")

    button_zaloguj = Button(root_login, text="Zaloguj", command=sprawdz_logowanie)

    label_tytul.grid(row=0, column=0, columnspan=2, pady=10)

    label_login.grid(row=1, column=0, padx=10, pady=5, sticky=E)
    entry_login.grid(row=1, column=1, padx=10, pady=5)

    label_haslo.grid(row=2, column=0, padx=10, pady=5, sticky=E)
    entry_haslo.grid(row=2, column=1, padx=10, pady=5)

    button_zaloguj.grid(row=3, column=0, columnspan=2, pady=15)

    entry_login.focus()

    root_login.mainloop()

    return zalogowano