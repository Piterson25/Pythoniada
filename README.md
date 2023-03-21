# Pythoniada

🎮 Gra typu "Familiada" napisana w Pythonie.

## 🗒️ Opis
Pythoniada to prosta gra napisana w Pythonie, naśladująca znany teleturniej "Familiada" z wszystkimi jego elementami. Gra odbywa się w oknie terminalu, a wyniki zapisywane są do pliku.

Na początku gry gracz jest proszony o podanie imienia, a następnie losowany jest suchar. Gra składa się z dwóch etapów, z których każdy składa się z pięciu pytań.

W pierwszym etapie gracz ma trzy próby na każde pytanie i zbiera punkty. Punkty są kumulowane, a jeśli gracz nie zna odpowiedzi na jakieś pytanie, może napisać "skip", aby je pominąć bez utraty czasu. Zarówno pytania, jak i punkty za odpowiedzi są losowe. Aby przejść do finału, gracz musi zdobyć przynajmniej 50 punktów.

W finale ponownie mamy do dyspozycji pięć pytań, ale na każde z nich mamy tylko jedną próbę. Aby wygrać należy zdobyć przynajmniej 15 punktów w finale. Wyniki graczy zapisywane są w pliku scoreboard.txt.

## 💻 Uruchomienie
Do uruchomienia gry należy uruchomić plik main.py. Gra składa się z dwóch etapów:

* Pierwszy etap znajduje się w pliku pierwszyetap.py.
* Drugi etap, czyli etap finałowy, znajduje się w pliku final.py.

Dodatkowe pliki:
* funkcje.py - zawiera funkcje wykorzystywane w pozostałych plikach .py.
* asserty.py - zawiera testy na asercje.

Pliki z pytaniami:

* pytania.txt - plik z pytaniami w pierwszym etapie gry.
* pytania_finalowe.txt - plik z pytaniami w etapie finałowym gry.

Pozostałe pliki:

* przywitanie.txt - zawiera tekst przywitania na początku gry.
* suchary.txt - zawiera dowcipy na początku gry.
* scoreboard.txt - zawiera wyniki graczy po finale.
