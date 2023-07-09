## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

Zapoznaj się z plikiem **functions.py**. Znajdziesz tam dwie funkcje. Były one jednak pisane,
przez bardzo niechlujnego programistę. Kod nie działa tak, jak powinien, a styl pozostawia wiele do życzenia.
Poprawą kodu zajmiemy się w dalszej części.
Najpierw sprawdźmy, jakie błędy pokaże nam statyczna analiza kodu (flake8).

* Zainstaluj flake8 w swoim wirtualnym środowisku.
* Sprawdź plik **functions.py** za pomocą narzędzia do statycznej analizy kodu (flake8).

Podpowiedź:
Jednym ze zgłoszonych błędów jest ten, dotyczący maksymalnej długości linii. Pep8 zaleca nie więcej niż 79 znaków.
W dzisiejszych czasach często zwiększa się tę liczbę do 120 znaków.
Jeśli chcesz ustawić inną długość lini niż domyślna możesz dodać do komendy flake8 flagę `--max-line-length`:

`flake8 <python-file> --max-line-length <number>`


## Zadanie 2.

Flake8 powinien znaleźć nam 21 błędów.

* Popraw wszystkie błędy.

#### Więcej informacji na temat kodów błędów znajdziesz tutaj:

[http://flake8.pycqa.org/en/latest/user/error-codes.html](http://flake8.pycqa.org/en/latest/user/error-codes.html)

## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

W dziale o statycznej analizie kodu mieliśmy plik **functions.py**. Znajdziesz w nim funkcję `div(a, b)`, 
która zwraca iloraz argumentów a i b.

1. Napisz testy jednostkowe, które przetestują tę funkcję. Testy powinny
    * sprawdzić, czy funkcja zwraca poprawny wynik dla dzielenia liczb całkowitych,
    * sprawdzić, czy funkcja zwraca poprawny wynik dla dzielenia liczb zmiennoprzecinkowych,
    * sprawdzić, czy funkcja dopuszcza dzielenie przez zero (powinien być wyrzucony odpowiedni wyjątek),
    * sprawdzić, czy funkcja poradzi sobie z liczbami zapisanymi jako `string`.

2. W zależnosci od wyników testów, popraw funkcję `div()`.


## Zadanie 2

W pliku **functions.py** znajduje się funkcja `analyze_pesel()`. 
Funkcja ta przyjmuje jeden parametr: numer PESEL, a zwraca słownik z następującymi kluczami:

* "pesel": wejściowy numer,
* "gender": płeć zakodowaną w numerze (male / female),
* "birth_date": datę urodzenia zakodowaną w numerze,
* "valid": czy numer jest poprawny.

Niestety – funkcja została napisana przez wyjątkowo niechlujnego programistę. Przetestuj funkcję i popraw błędy. 
W tym celu:
* Napisz testy jednostkowe, które sprawdzą: 
    * czy funkcja poprawnie waliduje numer pesel,
    * czy funkcja zwraca poprawne dane. 
* Pamiętaj, by przetestować numery osób urodzonych po 31 grudnia 1999 roku. 
* Popraw ewentualne błędy, aż wszystkie napisane przed chwilą testy przejdą.

#### Jeśli potrzebujesz pomocy, zajrzyj tutaj:

* [https://pl.wikipedia.org/wiki/PESEL#Numer_PESEL](https://pl.wikipedia.org/wiki/PESEL#Numer_PESEL) – zasady walidacji numeru PESEL,
* [http://pesel.felis-net.com](http://pesel.felis-net.com) – generator przykładowych numerów PESEL.

## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

* Napisz, używając techniki TDD, funkcję o nazwie **calculate_vat**. 
* Funkcja ma przyjmować dwa argumenty:
    * price - cena,
    * vat - stawka podatku VAT jako liczba całkowita.
* Funkcja powinna zwrócić kwotę podatku VAT do zapłaty.


## Zadanie 2

Napisz, używając techniki TDD, funkcję o nazwie **hash_password**. 
Funkcja powinna przyjmować hasło (w postaci zwykłego napisu), a zwracać hasz MD5 tegoż hasła. 

**Wymagania:**

* hasło ma mieć minimum 7 znaków,
* powinno zawierać:
    * przynajmniej jedną wielką literę,
    * przynajmniej jedną małą literę,
    * przynajmniej jedną cyfrę,
    * przynajmniej jeden znak specjalny z zakresu:
    `!@#$%^&*()_+-={}[]|\:";'<>?,./"`,
* funkcja ma zwrócić hasło zahaszowane przy użyciu algorytmu MD5 (sprawdź moduł **hashlib** w bibliotece standardowej),
* jeśli któryś z warunków hasła (długość lub obecność odpowiednich znaków) nie został spełniony, 
funkcja ma zwrócić `None`.

**Hint:** może pomóc Ci [funkcja `any()`](https://docs.python.org/3/library/functions.html#any).


## Zadanie 3

Wyobraź sobie, że Twój klient, dla którego pisałeś funkcję w poprzednim zadaniu, zażądał zmiany w kodzie:
 hasło musi mieć przynajmniej 8 znaków. Zgodnie z zasadą TDD, popraw testy, a potem kod programu.


## Zadanie 1 &ndash; rozwiązywane z wykładowcą.

#### Przygotowanie projektu

W katalogu **4_Django** znajduje się bardzo prosta aplikacja. Ma jeden model &ndash; produkt oraz trzy widoki:
* lista wszystkich produktów,
* formularz dodawania produktu,
* szczegółowy widok produktu.

Zapoznaj się z plikami w aplikacji, a następnie:
* zainstaluj `pytest-django`, jeśli jeszcze tego nie zrobiłeś,
* załóż bazę danych o nazwie tdd,
* sprawdź konfigurację aplikacji (baza danych itp),
* uruchom migracje.


## Zadanie 2 &ndash; rozwiązywane z wykładowcą.

Napisz test, który sprawdzi, czy szczegółowe dane produktu wyświetlają się poprawnie.
W tym celu:
* przygotuj fiksturę klienta django,
* przygotuj fiksturę, która doda jeden produkt do bazy danych,
* napisz test, który skorzysta z powyższych fikstur a następnie:
    * za pomocą klienta pójdzie pod odpowiedni adres metodą `get`,
    * sprawdzi, czy status odpowiedzi to 200,
    * sprawdzi, czy do kontekstu przekazano odpowiednie dane.
    
Podpowiedź: nie zapomnij oznaczyć test dekoratorem `django_db`.


## Zadanie 3

Napisz test, który sprawdzi, czy dodawanie do bazy danych działa.
Scenariusz testu:
* Pójdź na adres url: 'product/add/' metodą **POST**, przekazując odpowiednie dane w zapytaniu,
* Sprawdź, czy do bazy danych został dodany produkt, na podstawie tych danych,
* Sprawdź status odpowiedzi (zwróć uwagę, że używamy przekierowania, więc **302** będzie OK).

Nie zapomnij o odpowiednich fiksturach.
Nie zapomnij o oznaczeniu testu dekoratorem `django_db`.


## Zadanie 4

Napisz test, który sprawdzi, czy lista produktów wyświetla się poprawnie.
Scenariusz testu:
* Dodaj do bazy danych 3 produkty (stwórz w tym celu odpowiednią fiksturę),
* Pójdź na odpowiedni adres URL (pusty adres naszej aplikacji),
* Sprawdź status odpowiedzi,
* Sprawdź, czy do kontekstu przekazano produkty w odpowiedniej kolejności.

Nie zapomnij o odpowiednich fiksturach.
Nie zapomnij o oznaczeniu testu dekoratorem `django_db`.