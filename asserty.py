def lowercase(napis):
    napis2 = ''

    for i in range(len(napis)):
        if napis[i] >= 'A' and napis[i] <= 'Z':
            #ord - zamiana znaku na int
            napis2 += chr((ord(napis[i]) + 32))
        else:
            napis2 += napis[i]

    return napis2


def test_lower():
    napis = "WiTaMy barDZO serDeczNIe"
    assert lowercase(napis) == napis.lower()


def split(napis, separator):
    lista = []
    word = ''
    for znak in napis:
        if znak not in separator:
            word += znak
        elif word:
            lista.append(word)
            word = ''

    if word:
        lista.append(word)

    return lista


def test_split():
    napis = "54545454545; dsadadsadad; hahahaha; 5.32"
    assert split(napis, ";") == napis.split(";")


def czy_jest(szukany, lista):
    for e in lista:
        if e == szukany:
            return True
    return False


def test_in():
    lista = [5, 3, 3, 6, 7, 2, 1]
    assert czy_jest(3, lista) == (3 in lista)


def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                x = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = x
    return lista


def test_sort():
    lista = [5, 3, 3, 6, 7, 2, 1]
    assert bubble_sort(lista) == sorted(lista)


def dlugosc(lista):
    dl = 0
    for i in lista:
        dl += 1
    return dl


def test_len():
    lista = [5, 3, 6, 2, 8, 1, 0, 4, 1]
    assert dlugosc(lista) == len(lista)
