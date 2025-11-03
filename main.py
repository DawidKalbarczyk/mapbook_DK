import requests
import folium
from bs4 import BeautifulSoup





def nazwa_nowej_funkcji(operacja, users_data) -> None:
    match operacja:
        case "display":
            wyswietlanie_znajomych(users_data)
        case "add":
            print("Wybano funkcje dodawania znajomego")
            name:str = input("Podaj imie: ")
            location:str = input("Podaj lokalizacje: ")
            posts:int = int(input("Podaj ilość postów: "))
            img_url = input("Wprowadz adres URL zdjecia")
            users_data.append({
                "alias_name": name,
                "location": location,
                "posts": posts,
                "img_url": img_url
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
        case "wyswietl":
            prepare_map(users)
            "Stworzono mapę!"






def wyswietlanie_znajomych(users_data:list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["alias_name"]} z {user["location"]} opublikował {user['posts']} postów")






def get_coordinates(city_name:str)-> list:
    naglowek = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36 "
                      "(+https://twojastrona.pl/contact)"
    }

    url: str = f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(url, headers=naglowek)
    response_html = BeautifulSoup(response.text, "html.parser")
    # print(response_html.prettify())
    latitude = response_html.select('.latitude')
    latitude = float(latitude[1].text.replace(",", "."))
    longitude = response_html.select('.longitude')
    longitude = float(longitude[1].text.replace(",", "."))

    print(f"Latitude: {latitude}, Longitude: {longitude}")

    return [latitude, longitude]





def prepare_map(users_data:list) -> None:
    Map = folium.Map(location=[52.23, 21.0], zoom_start=6)

    for user in users_data:
        folium.Marker(
            location=get_coordinates(user["location"]),
            tooltip="Click me!",
            popup=
            f"""
                    <p style='font-size: 12px; color: red;'>User:
                    {user['alias_name']},</p> <p style='font-size: 10px; color: red;'>
                    {user['location']},</p> <p>{user['posts']}</p>
                    <img src={user['img_url']}
                    alt='1' style='width: 50px; height: 50px' />
                """,
            icon=folium.Icon(icon="", color="red"),
        ).add_to(Map)

    Map.save("notatnik.html")


users: list = [{
    "alias_name": "Dawid",
    "location": "Radom",
    "posts": 149,
    "img_url": ""
}, {
    "alias_name": "Kasia",
    "location": "Warszawa",
    "posts": 37,
    "img_url": ""
}, {
    "alias_name": "Michasia",
    "location": "Kraków",
    "posts": 1,
    "img_url": ""
}, {
    "alias_name": "Asia",
    "location": "Gdańsk",
    "posts": 1025,
    "img_url": ""
}]

while True:
    print("================================MENU=====================================")
    print("0. Wyjście z programu")
    print("1. Wyświetlenie aktywnych znajomych")
    print("2. Dodanie nowych znajomych")
    print("3. Usuwanie znajomych")
    print("4. Aktualizowanie znajomych")
    print("5. Generuj mapę znajomych")
    print("=========================================================================")
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
        case 5:
            nazwa_nowej_funkcji("wyswietl", users)




