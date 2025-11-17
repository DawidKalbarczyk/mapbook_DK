import requests
from bs4 import BeautifulSoup


def operation(operacja, users_data) -> None:
    match operacja:
        case "display":
            show_friends(users_data)
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
            show_friends(users_data)
        case "delete":
            print("Wybrano funkcje usuwania znajomych")
            tmp_name:str = input("Podaj imie uzytkownika do usunięcia ze znajomych: ")
            for user in users_data:
                if user["alias_name"] == tmp_name:
                    users_data.remove(user)
            show_friends(users_data)
        case "update":
            print("Wybrano funkcje aktualizowania znajomych")
            tmp_name:str = input("Podaj imie uzytkownik do aktualizacji: ")
            for user in users_data:
                if user["alias_name"] == tmp_name:
                    user["alias_name"] = input("Podaj nowe imie uzytkownika: ")
                    user["location"] = input("Podaj nową lokalizację uzytkownika: ")
                    user["posts"] = input("Podaj nową liczbę postów użytkownika: ")
            show_friends(users_data)
        case "wyswietl":
            prepare_map(users)
            "Stworzono mapę!"






def show_friends(users_data:list) -> None:
    print("=========================================================================")
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
    import folium
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

