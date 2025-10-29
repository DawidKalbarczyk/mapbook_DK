def nazwa_nowej_funkcji(operacja, users_data) -> None:
    match operacja:
        case "display":
            wyswietlanie_znajomych(users_data)
        case "add":
            print("Wybano funkcje dodawania znajomego")
            name:str = input("Podaj imie: ")
            location:str = input("Podaj lokalizacje: ")
            posts:int = int(input("Podaj ilość postów: "))
            users_data.append({
                "alias_name": name,
                "location": location,
                "posts": posts
            })
            wyswietlanie_znajomych(users_data)
        case "delete":
            print("Wybrano funkcje usuwania znajomych")
            tmp_name:str = input("Podaj imie uzytkownika do usunięcia ze znajomych: ")
            for user in users_data:
                if user["alias_name"] == tmp_name:
                    users_data.remove(user)
            wyswietlanie_znajomych(users_data)
        case "update":
            print("Wybrano funkcje aktualizowania znajomych")
            tmp_name:str = input("Podaj imie uzytkownik do aktualizacji: ")
            for user in users_data:
                if user["alias_name"] == tmp_name:
                    user["alias_name"] = input("Podaj nowe imie uzytkownika: ")
                    user["location"] = input("Podaj nową lokalizację uzytkownika: ")
                    user["posts"] = input("Podaj nową liczbę postów użytkownika: ")
            wyswietlanie_znajomych(users_data)

def wyswietlanie_znajomych(users_data:list) -> None:
    for user in users_data:
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
            nazwa_nowej_funkcji("display", users)
        case 2:
            nazwa_nowej_funkcji("add", users)
        case 3:
            nazwa_nowej_funkcji("delete", users)
        case 4:
            nazwa_nowej_funkcji("update", users)



