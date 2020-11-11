

# ECI-Toolbox

Wymagane moduły / Required modules:

- Pillow==8.0.1
- PyQt5==5.15.1
- PyQt5-sip==12.8.1
- PyQt5-stubs==5.14.2.2
- pyqt5-tools==5.15.1.1.7.5

## PL description below :)

## [EN] A word of introduction
ECI-Toolbox is a collection of programs that I wrote to make my work easier for myself and others in the company where I am currently employed. Their main assumption is to accelerate and facilitate repetitive boring tasks that I had to deal with every day. At the beginning, the plan was to create a UI with buttons like "choose what you want to do", but I figured that after me, people who do not require full functionality will use it - so there is no point.

- .prn - file format supported by label printers. It contains data such as coordinates, printout type, speed, etc.
.Prn files are specific to printers. Those in the /templates folder are supported by the TSC TC200 printer.
- .nxf - file format used by testers from Dynalab Inc. In practice this is xml.
- .nxb - as above, in practice this is .jpg with a changed extension.

There is still to be done:
- Code refactoring (I learned PyQt5 on these programs so the quality of the code may leave a lot to be desired)
- Added a program that converts .jpg files to .nxb files (Required for Nx Fixture Block Editor)

### CPS Generator.py
A program for generating .prn files based on a project selected by the user (projects use different sizes of labels) and data entered by the user.

Functions:
- Generating .prn files according to the pattern in /templates folder
- Displaying the character limit for a given label
- Placing generated files in a folder - after filling in the "Numer wiązki" field, otherwise the files are saved on the desktop
- Choosing the right patterns based on the number of completed lines (1/2/3)
- Direct printing without saving the file
#### The limits.py file is required to run the program!


### Employee code generator.py
Generating labels with the employee's code (barcode) and first and last name. The principle of operation is similar to CPS Generator.py, but with less functions.
Although the employee number should always represent a number, it has not been included in the code - sometimes this generator is used by the company
it is used for other purposes by generating barcode labels.

Functions:
- Generating .prn labels and saving them to the desktop.
- Direct printing without saving the file


### Image resizer.py
Reduce images by hard-coded value of 78%. Company needs :)
Functions:
- Shrink all pictures in a user-selected folder (filedialog) and place them on the desktop.


### Multiple labels generator.py
Generating labels according to a pattern defined by the user.
Example: Filling the field "Początek" as "CRP" and "Ilość sztuk" as 30 will give us the result of CRP1, CRP2, CRP3 ... CRP29, CRP30

Functions:
- Mass generation of labels according to the selected pattern and data entered by the user
- Placing all labels in a folder on the desktop


### .nxf with QR code generator
The program was written typically for the colleague from the office next door - that explains the turquoise background :) Generating .nxf file with user data.


#### Program Icon License:
<div> Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect"> Pixel perfect </a>

## [PL] Słowem wstępu
ECI-Toolbox to zbiór programów które napisałem aby ułatwić sobie i innym pracę w firmie gdzie jestem aktualnie zatrudniony. Główne ich założenie to przyspieszenie oraz ułatwienie powtarzalnych, nudnych zadań z którymi musiałem się mierzyć każdego dnia. Z początku plan był na stworzenie UI z przyciskami typu "wybierz co chcesz zrobić", jednak uznałem że po za mną samym będą korzystać z tego osoby które nie wymagają pełnej funkcjonalności - więc nie ma sensu.

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
Generowanie etykiet z kodem pracownika (kod kreskowy) oraz imieniem i nazwiskiem. Zasada działania podobna do CPS Generator.py, jednak bardziej okrojona z funkcji.
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
