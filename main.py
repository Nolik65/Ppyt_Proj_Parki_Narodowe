from tkinter import *
import tkintermapview

from Parki_Narodowe_lib.model import User, users

def show_users() -> None:
    listbox_lista_parkow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_parkow.insert(idx, user.park)


def remove_user() -> None:
    i = listbox_lista_parkow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    show_users()


def show_user_details():
    i = listbox_lista_parkow.index(ACTIVE)
    pracownicy = users[i].pracownicy
    goscie = users[i].goscie
    pojazdy = users[i].pojazdy
    park = users[i].park

    label_pracownicy_szczegoly_parku_wartosc.config(text=pracownicy)
    label_goscie_szczegoly_parku_wartosc.config(text=goscie)
    label_pojazdy_szczegoly_parku_wartosc.config(text=pojazdy)
    label_park_szczegoly_parku_wartosc.config(text=park)
    map_widget.set_position(users[i].coordinates[0], users[i].coordinates[1])
    map_widget.set_zoom(12)


def edit_user():
    i = listbox_lista_parkow.index(ACTIVE)
    pracownicy = users[i].pracownicy
    goscie = users[i].goscie
    pojazdy = users[i].pojazdy
    park = users[i].park

    entry_pracownicy.insert(0, pracownicy)
    entry_goscie.insert(0, goscie)
    entry_pojazdy.insert(0, pojazdy)
    entry_park.insert(0, park)

    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: update_user(i))


def update_user(i):
    users[i].pracownicy = entry_pracownicy.get()
    users[i].goscie = entry_goscie.get()
    users[i].pojazdy = entry_pojazdy.get()
    users[i].park = entry_park.get()
    users[i].coordinates = User.get_coordinates(users[i])
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].coordinates[0], users[i].coordinates[1], text=users[i].park)

    button_dodaj_uzytkownika.config(text="Dodaj uzytkownika", command=add_user)
    entry_pracownicy.delete(0, END)
    entry_goscie.delete(0, END)
    entry_pojazdy.delete(0, END)
    entry_park.delete(0, END)

    entry_pracownicy.focus()
    show_users()


def add_user():
    employees = entry_pracownicy.get()
    guests = entry_goscie.get()
    vehicles = entry_pojazdy.get()
    park = entry_park.get()

    new_user = User(pracownicy=employees, goscie=guests, pojazdy=vehicles, park=park)
    users.append(new_user)

    new_user.marker = map_widget.set_marker(new_user.coordinates[0], new_user.coordinates[1], text=new_user.park)

    entry_pracownicy.delete(0, END)
    entry_goscie.delete(0, END)
    entry_pojazdy.delete(0, END)
    entry_park.delete(0, END)

    entry_pracownicy.focus()
    show_users()


root = Tk()

root.title("Parki narodowe")
root.geometry("1024x760")

# FRAME
ramka_lista_parkow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_parku = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_parkow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_parku.grid(row=1, column=0, columnspan=2, padx=50, pady=20)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# RAMKA LISTA OBIEKTOW
label_lista_parkow = Label(ramka_lista_parkow, text="Lista parków narodowych: ")
listbox_lista_parkow = Listbox(ramka_lista_parkow)

button_pokaz_szczegoly_parku = Button(ramka_lista_parkow, text="Pokaż szczegóły parku", command=show_user_details)
button_usun_obiekt = Button(ramka_lista_parkow, text="Usun", command=remove_user)
button_edytuj_obiekt = Button(ramka_lista_parkow, text="Edytuj", command=edit_user)

label_lista_parkow.grid(row=0, column=0)
listbox_lista_parkow.grid(row=1, column=0)
button_pokaz_szczegoly_parku.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz, text="Formularz: ")
label_pracownicy = Label(ramka_formularz, text="Pracownicy: ")
label_goscie = Label(ramka_formularz, text="Goście: ")
label_pojazdy = Label(ramka_formularz, text="Marka pojazdów: ")
label_park = Label(ramka_formularz, text="Nazwa parku narodowego: ")

label_formularz.grid(row=0, column=0, columnspan=2)
label_pracownicy.grid(row=1, column=0, sticky=W)
label_goscie.grid(row=2, column=0, sticky=W)
label_pojazdy.grid(row=3, column=0, sticky=W)
label_park.grid(row=4, column=0, sticky=W)

entry_pracownicy = Entry(ramka_formularz)
entry_goscie = Entry(ramka_formularz)
entry_pojazdy = Entry(ramka_formularz)
entry_park = Entry(ramka_formularz)

entry_pracownicy.grid(row=1, column=1)
entry_goscie.grid(row=2, column=1)
entry_pojazdy.grid(row=3, column=1)
entry_park.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz, text="Dodaj park narodowy", command=add_user)
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# SZCZEGOLY OBIEKTU

label_szczegoly_parku = Label(ramka_szczegoly_parku, text="Szczegóły wybranego parku:")
label_pracownicy_szczegoly_parku = Label(ramka_szczegoly_parku, text="Pracownicy: ")
label_pracownicy_szczegoly_parku_wartosc = Label(ramka_szczegoly_parku, text="...")
label_goscie_szczegoly_parku = Label(ramka_szczegoly_parku, text="Goście: ")
label_goscie_szczegoly_parku_wartosc = Label(ramka_szczegoly_parku, text="...")
label_pojazdy_szczegoly_parku = Label(ramka_szczegoly_parku, text="Marki wjeżdżających samochodów gości: ")
label_pojazdy_szczegoly_parku_wartosc = Label(ramka_szczegoly_parku, text="...")
label_park_szczegoly_parku = Label(ramka_szczegoly_parku, text="Park: ")
label_park_szczegoly_parku_wartosc = Label(ramka_szczegoly_parku, text="...")

label_szczegoly_parku.grid(row=0, column=0, sticky=W)
label_pracownicy_szczegoly_parku.grid(row=1, column=0, sticky=W)
label_pracownicy_szczegoly_parku_wartosc.grid(row=1, column=1, sticky=W)
label_goscie_szczegoly_parku.grid(row=1, column=2, sticky=W)
label_goscie_szczegoly_parku_wartosc.grid(row=1, column=3, sticky=W)
label_pojazdy_szczegoly_parku.grid(row=1, column=4, sticky=W)
label_pojazdy_szczegoly_parku_wartosc.grid(row=1, column=5, sticky=W)
label_park_szczegoly_parku.grid(row=1, column=6, sticky=W)
label_park_szczegoly_parku_wartosc.grid(row=1, column=7, sticky=W)

# ramka mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=600, corner_radius=4)
map_widget.set_zoom(6)
map_widget.set_position(52.2, 21.0)
map_widget.grid(row=0, column=0)


root.mainloop()
