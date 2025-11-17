from mapbook_lib.controller import operation
from mapbook_lib.model import users


def main():
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
                operation("display", users)
            case 2:
                operation("add", users)
            case 3:
                operation("delete", users)
            case 4:
                operation("update", users)
            case 5:
                operation("wyswietl", users)
if __name__ == "__main__":
    main()



