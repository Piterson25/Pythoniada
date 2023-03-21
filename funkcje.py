import random, os


def suchar():
    wszystkich_sucharow = sum(1 for linia in open('suchary.txt', "r"))
    id_suchara = random.randint(1, wszystkich_sucharow)

    linijka = pisanie_jednej(id_suchara, "suchary.txt")

    wiersz = linijka.split(";")
    return wiersz


def czy_bylo_pytanie(nr, lista):
    for e in lista:
        if e == nr:
            return True
    return False


def pisanie_jednej(numer_liniki, nazwa_pliku):
    plik = open(nazwa_pliku)
    wiersz = plik.readlines()
    plik.close()
    return wiersz[numer_liniki - 1]


def znajdzAnswer(odp_gracza, lista_odpowiedzi):
    for odp in lista_odpowiedzi:
        if odp_gracza == odp:
            return True
    return False


def zapisWyniku(imie, wynik, nazwa_pliku):
    wynik = str(wynik)
    f = open(nazwa_pliku, "a")
    f.write(imie + " " + wynik + "\n")
    f.close()


def odczyt_rekordu(nazwa_pliku):
    wiersze = {}
    suma_wierszy = sum(1 for linia in open(nazwa_pliku, "r"))
    for i in range(1, suma_wierszy + 1):
        linijka = pisanie_jednej(i, nazwa_pliku)
        rekord = linijka.split()
        wiersze[rekord[0]] = int(rekord[1])
    return max(wiersze.values())


# funkcja czyszczaca ekran
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def sortowanie(slownik):
    lista = list(slownik.items())
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][1] < lista[j][1]:
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
        posortowane = dict(lista)
    return posortowane
