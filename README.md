# Pythoniada

🎮 Gra typu "Familiada" napisana w Pythonie.

## 🗒️ Opis
Pythoniada to prosta gra napisana w Pythonie, naśladująca znany teleturniej "Familiada" z wszystkimi jego elementami. Gra odbywa się w oknie terminalu, a wyniki zapisywane są do pliku.

Na początku gry gracz jest proszony o podanie imienia, a następnie losowany jest suchar. Gra składa się z dwóch etapów, z których każdy składa się z 5 pytań.

W pierwszym etapie gracz ma 3 próby na każde pytanie i zbiera punkty. Punkty są kumulowane, a jeśli gracz nie zna odpowiedzi na jakieś pytanie, może napisać "skip", aby je pominąć. Zarówno pytania, jak i punkty za odpowiedzi są losowe. Aby przejść do finału, gracz musi zdobyć przynajmniej 50 punktów.

W finale ponownie mamy do dyspozycji 5 pytań, ale na każde z nich mamy tylko 1 próbę. Aby wygrać należy zdobyć przynajmniej 15 punktów w finale. Wyniki graczy zapisywane są w pliku [scoreboard.txt](https://github.com/Piterson25/Pythoniada/blob/main/scoreboard.txt).

## 💻 Uruchomienie
Do uruchomienia gry należy uruchomić plik [main.py](https://github.com/Piterson25/Pythoniada/blob/main/main.py). Gra składa się z dwóch etapów:

* Pierwszy etap znajduje się w pliku [pierwszyetap.py](https://github.com/Piterson25/Pythoniada/blob/main/pierwszyetap.py).
* Drugi etap, czyli etap finałowy, znajduje się w pliku [final.py](https://github.com/Piterson25/Pythoniada/blob/main/final.py).

Dodatkowe pliki:
* [funkcje.py](https://github.com/Piterson25/Pythoniada/blob/main/funkcje.py) - zawiera funkcje wykorzystywane w pozostałych plikach .py.
* [asserty.py](https://github.com/Piterson25/Pythoniada/blob/main/asserty.py) - zawiera testy na asercje.

Pliki z pytaniami:

* [pytania.txt](https://github.com/Piterson25/Pythoniada/blob/main/pytania.txt) - plik z pytaniami w pierwszym etapie gry.
* [pytania_finalowe.txt](https://github.com/Piterson25/Pythoniada/blob/main/pytania_finalowe.txt) - plik z pytaniami w etapie finałowym gry.

Pozostałe pliki:

* [przywitanie.txt](https://github.com/Piterson25/Pythoniada/blob/main/przywitanie.txt) - zawiera tekst przywitania na początku gry.
* [suchary.txt](https://github.com/Piterson25/Pythoniada/blob/main/suchary.txt) - zawiera dowcipy na początku gry.
* [scoreboard.txt](https://github.com/Piterson25/Pythoniada/blob/main/scoreboard.txt) - zawiera wyniki graczy po finale.
