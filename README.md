

# ECI-Toolbox

Wymagane moduły:

- Pillow==8.0.1
- PyQt5==5.15.1
- PyQt5-sip==12.8.1
- PyQt5-stubs==5.14.2.2
- pyqt5-tools==5.15.1.1.7.5

## PL description below :)
## Słowem wstępu
ECI-Toolbox to zbiór programów które napisałem aby ułatwić sobie i innym pracę w firmie gdzie jestem aktualnie zatrudniony. Główne ich założenie to przyspieszenie oraz ułatwienie powtarzalnych, nudnych zadań z którymi musiałem się mierzyć każdego dnia. Z początku plan był na stworzenie UI z przyciskami typu "wybierz co chcesz zrobić", jednak uznałem że skoro osoby które będą korzystać z tych programów nie będą używały wszystkich opcji to nie ma sensu.

- .prn - format pliku obsługiwany przez drukarki do etykiet. Zapisane są w nim dane typu koordynaty, typ wydruku, szybkość itp.  
Pliki .prn są specyficzne dla konkretnych drukarek. Te zawarte w folderze /templates są obsługiwane przez drukarkę TSC TC200.
- .nxf - format pliku używany przez testery firmy Dynalab Inc. W praktyce jest to xml.
- .nxb - jak wyżej, w praktyce jest to .jpg z zmienionym rozszerzeniem

Do zrobienia zostało:
- Refaktoryzacja kodu (Uczyłem się PyQt5 na tych programach więc jakość kodu może pozostawiać wiele do życzenia)
- Dodanie programu konwertującego pliki .jpg na .nxb (Wymagane dla programu Nx Fixture Block Editor)

### CPS Generator.py
Program służący do generowania plików .prn na podstawie wybranego przez użytkownika projektu (projekty korzystają z różnych rozmiarów etykiet) oraz danych przez niego wpisanych.

Funkcje:
- Generowanie plików .prn według wzoru umieszczonego w /templates
- Wyświetlanie limitu znaków dla danej etykiety
- Umieszczanie wygenerowanych plików w folderze - po uzupełnieniu pola "Numer wiązki", w przeciwnym razie pliki zapisują się na pulpicie
- Dobieranie odpowiednich wzorów na postawie ilości uzupełnionych linijek (1/2/3)
- Bezpośrednie drukowanie bez zapisu pliku 
#### Do działania programu wymagany jest plik limits.py!


### Employee code generator.py
Generowanie etykiet z kodem pracownika oraz imieniem i nazwiskiem. Zasada działania podobna do CPS Generator.py, jednak bardziej okrojona z funkcji.
Mimo iż numer pracownika powinien zawsze reprezentować liczbę nie zostało to umieszczone w kodzie - na potrzeby firmy czasem ten generator
jest wykorzystywany do innych celów z racji generowania etykiet z kodem kreskowym.

Funkcje:
- Generowanie etykiet .prn i zapisywanie ich na pulpicie.
- Bezpośrednie drukowanie bez zapisu pliku


### Image resizer.py
Zmniejszanie zdjęć o zakodowaną na stałe wartość 78%. Potrzeby firmy :)
Funkcje:
- Zmniejszanie wszystkich zdjęć w folderze wybranym przez użytkownika (filedialog) i umieszczanie ich na pulpicie.


### Multiple labels generator.py
Generowanie etykiet według ustalonego przez użytkownika wzoru.
Przykład: Uzupełnienie pola "Początek" jako "CRP", oraz "Ilość sztuk" jako 30 da nam rezultat CRP1, CRP2, CRP3 ... CRP29, CRP30

Funkcje: 
- Masowe generowanie etykiet według wybranego wzoru oraz danych wprowadzonych przez użykownika
- Umieszczanie wszystkich etykiet w folderze na pulpicie


### .nxf with QR code generator
Program napisany typowo dla koleżanki z biura obok - to tłumaczy turkosowe tło :) Generowanie pliku .nxf z danymi użytkownika.


#### Licencja ikony programu:
<div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a>
