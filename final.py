import time
from funkcje import *


def final(imie):
    punkty = 0
    uzyte_pytania = []

    clear()
    time.sleep(2)

    maks_punktow = odczyt_rekordu("scoreboard.txt")
    print("Twoj obecny rekord w finale wynosi: " + str(maks_punktow) + " punktow")
    time.sleep(2)

    print("Rozpoczynamy final Pythoniady!")
    time.sleep(2)

    clear()
    time.sleep(1)

    #krotka
    twoje_punkty = ()

    for nr_pytania in range(1, 6):
        wszystkich_pytan = sum(1 for linia in open('pytania_finalowe.txt', "r"))  # assert

        id_pytania = random.randint(1, wszystkich_pytan)
        while czy_bylo_pytanie(id_pytania, uzyte_pytania):
            id_pytania = random.randint(1, wszystkich_pytan)
        uzyte_pytania.append(id_pytania)

        linijka = pisanie_jednej(id_pytania, "pytania_finalowe.txt")

        lista = linijka.split(";")  # assert
        pytanie = lista[0]

        odpowiedzi = {}

        for odp in range(1, len(lista) - 1):
            lista[odp] = lista[odp][1:]
            odpowiedzi[lista[odp]] = random.randint(1, 10)

        odpowiedzi = sortowanie(odpowiedzi)

        print(pytanie)

        while True:
            odp_gracza = input("> ")

            if znajdzAnswer(odp_gracza.lower(), odpowiedzi):
                punkty += odpowiedzi[odp_gracza.lower()]
                twoje_punkty += (odpowiedzi[odp_gracza.lower()], )
                print("\n")
                break
            else:
                twoje_punkty += (0, )
                print("\n")
                break

    time.sleep(1)
    clear()
    print("Lacznie udalo sie tobie zebrac...")

    time.sleep(1)
    print(str(punkty) + " punktow\n")

    time.sleep(1)
    print("Punktacja:")
    i = 1
    for x in twoje_punkty:
        print("Pytanie nr " + str(i) + "\t" + str(x))
        i += 1
    print()

    time.sleep(1)
    zapisWyniku(imie, punkty, "scoreboard.txt")

    if punkty > 15:
        print("GRATULACJE WYGRALES/AS FINAL!!!\n")
        time.sleep(1)
        print("Twoj wynik zostal zapisany do tablicy wynikow.")
        time.sleep(2)
        print("Dziekujemy za gre! :)")
    else:
        print("Przykro mi, nie udalo sie Tobie wygrac gry D:")
