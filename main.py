def nazwa_nowej_funkcji(operacja, users_data):
    match operacja:
        case "wyswietl":
            wyswietlanie_znajomych(users_data)
        case "dodanie":
            print("Wybano funkcje dodawania znajomego")
            nowe_imie:str = input("Podaj imie: ")
            nowa_lokacja:str = input("Podaj lokalizacje: ")
            nowa_ilosc_postow:int = int(input("Podaj ilość postów: "))
            users_data.append({
                "alias_name": nowe_imie,
                "location": nowa_lokacja,
                "posts": nowa_ilosc_postow
            })
            wyswietlanie_znajomych(users_data)


def wyswietlanie_znajomych(users_data_second):
    for user in users_data_second:
        print(f"Twój znajomy {user["alias_name"]} z {user["location"]} opublikował {user['posts']} postów")


users: list = [{
    "alias_name": "Dawid",
    "location": "Radom",
    "posts": 149
}, {
    "alias_name": "Kasia",
    "location": "Warszawa",
    "posts": 37
}, {
    "alias_name": "Michasia",
    "location": "Kraków",
    "posts": 1
}, {
    "alias_name": "Asia",
    "location": "Gdańsk",
    "posts": 1025
}]

while True:
    tmp_choice:int = int(input("Wybierz opcje menu: "))
    match tmp_choice:
        case 0:
            break
        case 1:
            nazwa_nowej_funkcji("wyswietl")
        case 2:
            nazwa_nowej_funkcji("dodanie")
        case 3:
            print("Wybrano funkcje usuwania znajomych")
        case 4:
            print("Wybrano funkcje aktualizowania znajomych")



