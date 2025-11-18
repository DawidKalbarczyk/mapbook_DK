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





root = Tk()

root.title("Mapbook")
root.geometry("1025x600")

ramkaListaObiektów = Frame(root)
ramkaFormularz = Frame(root)
ramkaSzczegolyObiektu = Frame(root)
ramkaMapa = Frame(root)

ramkaListaObiektów.grid(row = 0, column = 0)
ramkaFormularz.grid(row = 0, column = 1)
ramkaSzczegolyObiektu.grid(row = 1, column = 0)
ramkaMapa.grid(row = 2, column = 0)

#RAMKA LISTA OBIEKTÓW
labelListaObiektow = Label(ramkaListaObiektów, text="Lista Obiektów")
labelListaObiektow.grid(row = 0, column = 0, columnspan = 3)

listBoxListaObiektow = Listbox(ramkaListaObiektów)
listBoxListaObiektow.grid(row = 1, column = 0, columnspan = 3)

buttonPokazSzczegoly = Button(ramkaListaObiektów, text="Pokaż szczegóły")
buttonPokazSzczegoly.grid(row=2, column = 0)

buttonUsunObiekt = Button(ramkaListaObiektów, text="Usuń obiekt")
buttonUsunObiekt.grid(row=2, column=1)

buttonEdytujObiekt = Button(ramkaListaObiektów, text="Edytuj obiekt")
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

buttonDodajObiekt = Button(ramkaFormularz, text="Dodaj obiekt")
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





