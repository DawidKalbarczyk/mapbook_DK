# from mapbook_lib.controller import operation
# from mapbook_lib.model import users
#
#
# def main():
#     while True:
#         print("================================MENU=====================================")
#         print("0. Wyjście z programu")
#         print("1. Wyświetlenie aktywnych znajomych")
#         print("2. Dodanie nowych znajomych")
#         print("3. Usuwanie znajomych")
#         print("4. Aktualizowanie znajomych")
#         print("5. Generuj mapę znajomych")
#         print("=========================================================================")
#         tmp_choice:int = int(input("Wybierz opcje menu: "))
#         match tmp_choice:
#             case 0:
#                 break
#             case 1:
#                 operation("display", users)
#             case 2:
#                 operation("add", users)
#             case 3:
#                 operation("delete", users)
#             case 4:
#                 operation("update", users)
#             case 5:
#                 operation("wyswietl", users)
# if __name__ == "__main__":
#     main()
#


from tkinter import *
import tkintermapview
import requests
from  bs4 import BeautifulSoup
users:list = []

class User:
    def __init__(self, name: str, location: str, posts: int, img_url: str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_coordinates()



    def get_coordinates(self):
        import requests
        from bs4 import BeautifulSoup

        naglowek = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0 Safari/537.36 "
                          "(+https://twojastrona.pl/contact)"
        }

        url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(url, headers=naglowek)
        response_html = BeautifulSoup(response.text, "html.parser")
        # print(response_html.prettify())
        latitude = response_html.select('.latitude')
        latitude = float(latitude[1].text.replace(",", "."))
        longitude = response_html.select('.longitude')
        longitude = float(longitude[1].text.replace(",", "."))

        print(f"Latitude: {latitude}, Longitude: {longitude}")

        return [latitude, longitude]

def add_user(users_data:list)->None:
    name: str = entryImie.get()
    location: str = entryLokalizacja.get()
    posts: int = int(entryPosty.get())
    img_url: str = entryIMG_URL.get()
    users_data.append(User(name=name, location=location, posts=posts, img_url=img_url))
    print(users_data)
    user_info(users_data)
    entryImie.delete(0, END)
    entryLokalizacja.delete(0, END)
    entryPosty.delete(0, END)
    entryIMG_URL.delete(0, END)
    entryImie.focus()

def user_info(users_data:list)->None:
    listBoxListaObiektow.delete(0, END)
    for idx, user in enumerate(users_data):
        listBoxListaObiektow.insert(idx, f"{idx+1}. {user.name} {user.location} {user.posts}")


def delete_user(users_data:list)->None:
    i = listBoxListaObiektow.index(ACTIVE)
    users_data.pop(i)
    user_info(users_data)

def user_details(users_data:list):
    i = listBoxListaObiektow.index(ACTIVE)
    labelImieSzczegolyObiektuWartosc.config(text=users[i].name)
    labelLokalizacjaSzczegolyObiektuWartosc.config(text=users[i].location)
    labelPostySzczegolyObiektuWartosc.config(text=users[i].posts)
    labelIMG_URL.config(text=users[i].img_url)

def edit_user(users_data:list):
    i = listBoxListaObiektow.index(ACTIVE)
    entryImie.insert(0, users_data[i].name)
    entryLokalizacja.insert(0, users_data[i].location)
    entryPosty.insert(0, users_data[i].posts)
    entryIMG_URL.insert(0, users_data[i].img_url)

    buttonDodajObiekt.config(text = "Zapisz zmiany", command=lambda: update_user(users_data, i))


def update_user(users_data:list, i)->None:
    users_data[i].name = entryImie.get()
    users_data[i].location = entryLokalizacja.get()
    users_data[i].posts = entryPosty.get()
    users_data[i].img_url = entryIMG_URL.get()
    user_info(users_data)
    buttonDodajObiekt.config( text="Dodaj obiekt", command=lambda: add_user(users))

    entryImie.delete(0, END)
    entryLokalizacja.delete(0, END)
    entryPosty.delete(0, END)
    entryIMG_URL.delete(0, END)
    entryImie.focus()
root = Tk()

root.title("Mapbook")
root.geometry("1025x600")

ramkaListaObiektów = Frame(root)
ramkaFormularz = Frame(root)
ramkaSzczegolyObiektu = Frame(root)
ramkaMapa = Frame(root)

ramkaListaObiektów.grid(row = 0, column = 0, columnspan=2)
ramkaFormularz.grid(row = 0, column = 1)
ramkaSzczegolyObiektu.grid(row = 1, column = 0, columnspan=2)
ramkaMapa.grid(row = 2, column = 0, columnspan=2)

#RAMKA LISTA OBIEKTÓW
labelListaObiektow = Label(ramkaListaObiektów, text="Lista Obiektów")
labelListaObiektow.grid(row = 0, column = 0, columnspan = 3)

listBoxListaObiektow = Listbox(ramkaListaObiektów)
listBoxListaObiektow.grid(row = 1, column = 0, columnspan = 3)

buttonPokazSzczegoly = Button(ramkaListaObiektów, text="Pokaż szczegóły", command=lambda: user_details(users))
buttonPokazSzczegoly.grid(row=2, column = 0)

buttonUsunObiekt = Button(ramkaListaObiektów, text="Usuń obiekt", command=lambda: delete_user(users))   #Musi być lambda
buttonUsunObiekt.grid(row=2, column=1)

buttonEdytujObiekt = Button(ramkaListaObiektów, text="Edytuj obiekt", command=lambda: edit_user(users, i))
buttonEdytujObiekt.grid(row=2, column=2)




#RAMKA FORLUMARZ
labelFormularz = Label(ramkaFormularz, text="Formularz: ")
labelFormularz.grid(row=0, column=0, columnspan=2)

labelImie = Label(ramkaFormularz, text="Imie: ")
labelImie.grid(row=1, column=0, sticky=W)

labelLokalizacja = Label(ramkaFormularz, text="Lokalizacja: ")
labelLokalizacja.grid(row=2, column=0, sticky=W)

labelPosty = Label(ramkaFormularz, text="Posty: ")
labelPosty.grid(row=3, column = 0, sticky=W)

labelIMG_URL = Label(ramkaFormularz, text="Obrazek: ")
labelIMG_URL.grid(row=4, column = 0, sticky=W)

entryImie = Entry(ramkaFormularz)
entryImie.grid(row=1, column = 1)

entryLokalizacja = Entry(ramkaFormularz)
entryLokalizacja.grid(row=2, column=1)

entryPosty = Entry(ramkaFormularz)
entryPosty.grid(row=3, column=1)

entryIMG_URL = Entry(ramkaFormularz)
entryIMG_URL.grid(row=4, column=1)

buttonDodajObiekt = Button(ramkaFormularz, text="Dodaj obiekt", command=lambda: add_user(users))
buttonDodajObiekt.grid(row=5, column=0, columnspan=2)




#RAMKA SZCZEGÓłY OBIEKTU

labelSzczegolyObiektu = Label(ramkaSzczegolyObiektu, text="Szczegóły obiektu")
labelSzczegolyObiektu.grid(row=0, column=0, sticky=W)




labelImieSzczegolyObiektu = Label(ramkaSzczegolyObiektu, text="Imie: ")
labelImieSzczegolyObiektu.grid(row=1, column=0)

labelImieSzczegolyObiektuWartosc = Label(ramkaSzczegolyObiektu, text = "....")
labelImieSzczegolyObiektuWartosc.grid(row=1, column=1)




labelLokalizacjaSzczegolyObiektu = Label(ramkaSzczegolyObiektu, text="Lokalizacja: ")
labelLokalizacjaSzczegolyObiektu.grid(row=1, column=2)

labelLokalizacjaSzczegolyObiektuWartosc = Label(ramkaSzczegolyObiektu, text="....")
labelLokalizacjaSzczegolyObiektuWartosc.grid(row=1, column=3)




labelPostySzczegolyObiektu = Label(ramkaSzczegolyObiektu, text="Posty: ")
labelPostySzczegolyObiektu.grid(row=1, column=4)

labelPostySzczegolyObiektuWartosc = Label(ramkaSzczegolyObiektu, text="....")
labelPostySzczegolyObiektuWartosc.grid(row=1, column=5)


# RAMKA MAPY

mapWidget = tkintermapview.TkinterMapView(ramkaMapa, width = 1025, height=600, corner_radius=0)
mapWidget.set_position(52.0, 21.0)
mapWidget.set_zoom(6)
mapWidget.grid(row=0, column=0)



root.mainloop()





