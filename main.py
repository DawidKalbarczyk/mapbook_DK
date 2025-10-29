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

for user in users:
    print(f"Twój znajomy {user["alias_name"]} z {user["location"]} opublikował {user['posts']} postów")
