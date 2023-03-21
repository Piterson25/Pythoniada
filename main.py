from pierwszyetap import *


def start():
    imie = input("Podaj swoje imie: ")

    plik = open("przywitanie.txt", "r")
    print(plik.read())
    plik.close()

    while True:
        ready = input("Czy jestes gotowy/a do rozpoczecia gry, " + imie + "? (tak/nie)\n> ")
        if ready.lower() == "tak":
            clear()
            time.sleep(1)
            print("Pora na suchara: ")
            time.sleep(1)
            sucharek = suchar()
            print(sucharek[0])
            time.sleep(2)
            print(sucharek[1][1:])
            time.sleep(2)
            print("\n*smianie sie mp3*")
            time.sleep(2)
            pierwszy_etap(imie)
            break
        elif ready.lower() == "nie":
            print("No to do widzenia :)")
            break


start()

while True:
    w = input("")
