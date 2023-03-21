from final import *


def pierwszy_etap(imie):
    punkty = 0
    uzyte_pytania = []

    for nr_pytania in range(1, 6):
        clear()
        time.sleep(1)

        zycia = 3

        wszystkich_pytan = sum(1 for linia in open('pytania.txt', "r"))

        id_pytania = random.randint(1, wszystkich_pytan)

        while czy_bylo_pytanie(id_pytania, uzyte_pytania):
            id_pytania = random.randint(1, wszystkich_pytan)
        uzyte_pytania.append(id_pytania)

        linijka = pisanie_jednej(id_pytania, "pytania.txt")

        lista = linijka.split(";")
        pytanie = lista[0]

        odpowiedzi = {}

        for odp in range(1, len(lista) - 1):
            lista[odp] = lista[odp][1:]
            odpowiedzi[lista[odp]] = random.randint(1, 10)

        odpowiedzi = sortowanie(odpowiedzi)

        print("Pytanie numer", nr_pytania, "(" + str(len(odpowiedzi)) + " odpowiedzi)")

        time.sleep(1)
        print(pytanie + "\n")

        while True:
            odp_gracza = input("> ")

            if znajdzAnswer(odp_gracza.lower(), odpowiedzi):
                time.sleep(1)
                pkt_za_pytanie = odpowiedzi[odp_gracza.lower()]
                punkty += odpowiedzi[odp_gracza.lower()]
                odpowiedzi.pop(odp_gracza.lower())
                print("Brawo! Zdobyles/as " + str(pkt_za_pytanie) + " punktow\n")
                if len(odpowiedzi) == 0:
                    print("Udalo sie tobie napisac wszystkie odpowiedzi, szacun!")
                    time.sleep(3)
                    print("Konczysz ta runde z wynikiem " + str(punkty) + " punktow")
                    time.sleep(2)
                    break

            else:
                time.sleep(1)
                if odp_gracza.lower() == "skip":
                    print("Niestety nie znasz odpowiedzi na pozostale pytania :(")
                    time.sleep(1)
                    print("Pozostalymi odpowiedziami byly:")
                    time.sleep(1)
                    for e in odpowiedzi:
                        print("\t" + e + " za " + str(odpowiedzi[e]) + " pkt")
                    time.sleep(3)
                    print("Konczysz ta runde z wynikiem " + str(punkty) + " punktow")
                    time.sleep(2)
                    break
                else:
                    zycia -= 1
                    if zycia == 0:
                        print("Niestety nie udalo sie Tobie podac wszystkich odpowiedzi :(")
                        time.sleep(1)
                        print("Pozostalymi odpowiedziami byly:")
                        time.sleep(1)
                        for e in odpowiedzi:
                            print("\t" + e + " za " + str(odpowiedzi[e]) + " pkt")
                        time.sleep(3)
                        print("Konczysz ta runde z wynikiem " + str(punkty) + " punktow")
                        time.sleep(2)
                        break
                    print("Utrata zycia! Zostalo tobie", zycia, "zycia!\n")

            if len(odpowiedzi) == 0:
                break

    time.sleep(2)
    clear()
    print("Lacznie zebrale/as: " + str(punkty) + " punktow")
    time.sleep(1)

    if punkty > 50:
        print("A to oznacza dostanie sie do finalu! :D\n")
        time.sleep(1)
        while True:
            ready = input("Czy jestes gotowy do gry w finale? (tak/nie)\n> ")
            if ready.lower() == "tak":
                final(imie)
                break
            elif ready.lower() == "nie":
                print("No to do widzenia :)")
                break
    else:
        time.sleep(1)
        print("Niestety, zmuszony jestem Ciebie pozegnac :(")
        print("Masz za malo punktow by wejsc do finalu")
