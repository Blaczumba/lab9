# Zadania do wykonania podczas laboratorium 10

## Zadanie 1.

Celem zadania 1. jest stworzenie wstępnej wersji bazy danych o ludziach i ich relacjach rodzinnych.

W obecnej postaci ma się składać z dwóch klas:

 - `Person` zawiera informacje o osobie - identyfikator, nazwę, datę urodzenia, listę dzieci, ojca, oraz matkę.
 
 - `Database` zawiera słownik mapujący identyfikatory na osoby


Klasy `Person` oraz `Database` powinny być zgodne z testami w plikach `test_classes.py`, co oznacza że:

 - klasa `Person`:
 
   - powinna mieć konstruktor przyjmujący opcjonalnie wszystkie parametry poza listą dzieci
   
   - powinna mieć metody dostępu do kolejnych atrybutów
   
   - danych o rodzicach jakiejś osoby możemy nie mieć w bazie, więc pola z informacjami o nich mogą przyjmować wartość `None`.

   - powinna mieć metody umożliwiające ustawienie matki oraz ojca

   - metody ustawiające rodziców oraz konstruktor powinny dodawać osobę do listy dzieci rodzica
   
 - Klasa `Database`:
 
   - powinna mieć konstruktor przyjmujący opcjonalnie kolekcję osób
   
   - powinna miec metodę dostępu do osoby o zadanym id
   
   - powinna mieć metodę dostępu do kolekcji osób

   - powinna mieć metodę umożliwiającą dodanie ososby


## Zadanie 2.

Powinna być możliwość wczytania oraz zapisania bazy danych jako pliku .csv. 

Napisz funkcję `read_database_from_file` umożliwiającą wczytanie obiektu klasy `Database` z podanego uchwytu pliku w formacie csv. 

Napisz funkcję `write_database_to_file` umożliwiającą zapisanie obiektu klasy `Database` do podanego uchwytu pliku w formacie csv.

Nazwy pól powinny być następujące:

 - `id`
 
 - `name`
 
 - `birth_date`
 
 - `father_id`
 
 - `mother_id`


Podczas wczytywania bazy danych listy dzieci powinny zostać automatycznie wypełnione.

## Zadanie 3.

Zmodyfikuj klasę z zadania 1. aby korzystała z dat w postaci obiektów `datetime.date`. Można założyć że daty w pliku csv będą w formacie ISO: `YYYY-MM-DD`, co pozwala użyć funkcji `date.fromisoformat` do wczytywania.

Następnie napisz `Person` metodę umożliwiającą pobranie najstarszej osoby z rodzeństwa (jeżeli jest jedynakiem metoda powinna zwracać wartość `None`).

## Zadanie 4.

Napisz metodę umożliwiającą pobranie drzewa przodków danej osoby.

Następnie napisz funkcję, która zapisuje drzewo przodków danej osoby w postaci pliku YAML.

Do wykonania tego zadania jest potrzebny moduł PyYAML (`pip install PyYAML`).

Przykładowo, dla bazy osób:

```
id,name,birth_date,father_id,mother_id
1,Jan Kowalski,1960-06-01,,
2,Anna Wiśniewska,1962-01-06,,
3,Adam Kowalski,1984-03-03,1,2
4,Janina Nowak,1980-12-24,,
5,Stefan Kowalski,2004-07-28,3,4
```

dla osoby _Stefan Nowak_ powinien zostać utworzony następujący plik (kolejność pól zmodyfikowana dla poprawy czytelności):

```
id: '5'
name: Stefan Kowalski
birth_date: 2004-07-28
father:
  id: '3'
  name: Adam Kowalski
  birth_date: 1984-03-03
  father:
    id: '1'
    name: Jan Kowalski
    birth_date: 1960-06-01
  mother:
    id: '2'
    name: Anna Wisniewska
    birth_date: 1962-01-06
mother:
  id: '4'
  name: Janina Nowak
  birth_date: 1980-12-24
```