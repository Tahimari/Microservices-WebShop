# Microservices-WebShop

Aplikacja dostępna pod adresem:
http://3.120.148.31/

[![Build Status](https://travis-ci.com/Tahimari/Microservices-WebShop.svg?branch=master)](https://travis-ci.com/Tahimari/Microservices-WebShop)

Tematem projektu była implementacja sklepu internetowego.  
Sklep pozwala na stworzenie konta użytkownika, zalogowanie się do systemu, przeglądanie oraz zakup produktu.
Aplikacja posiada formularz kontaktowy, z którego mogą korzystać nawet niezalogowani użytkownicy.

Dla uprawnionych użytkowników (administratorów) dostępny jest również panel administracyjny.
Wśród opcji dostępnych w panelu administracyjnym jest m. in. możliwość dodania informacji o nowym produkcie.

Aplikację cechuje responsywny frontend i skalowalny backend.

Wykorzystane technologie:  
1. Frontend - Vue.js
2. Backend - Python + Flask
3. Bazy danych - SQLite, PostgreSQL

Część backendowa składa się z 4 mikroserwisów:
1. Użytkownicy (users) -> Flask + PostgreSQL
2. Produkty (products) -> Flask + Sqlite
3. Zamówienia (orders) -> Flask + Sqlite
4. Dostawa (shipments) -> Flask + Sqlite

Program został zaprojektowany w oparciu o architekturę mikroserwisową.
Mikroserwisy są aplikacjami typu [WebAPI](https://en.wikipedia.org/wiki/Web_API).
Każdy z mikroserwisów, po otrzymaniu żądania zwraca dane wyjściowe w formacie [JSON](https://www.json.org/).

Proces budowy aplikacji został zautomatyzowany dzięki wykorzystaniu narzędzia docker.
Jedyne co trzeba zrobić, to wywołać komendę docker-compose (z odpowiednimi parametrami).

Wszystkie zależności, potrzebne dla danego mikroserwisu, są zabudowane bezpośrednio w odpowiedni kontener. Każdy kontener dockera reprezentuje pojedynczy mikroserwis.

Strona jest hostowana w chmurze obliczeniowej (Amazon EC2), natomiast zdjęcia produktów są pobierane z serwisu Amazon S3.
Autoryzacja użytkowników odbywa się za pomocą tokena JWT, generowanego w serwisie użytkowników.
Token jest następnie przechowywany w plikach tymczasowych (tzw. local storage) przeglądarki.

## Jak zbudować projekt:

### Pobierz repozytorium:
``` git clone https://github.com/Tahimari/Microservices-WebShop.git ```
### Zaintaluj pakiety npm:
``` npm install front-service-vue ```
### Zbuduj i uruchom aplikację
``` docker-compose up -d --build ```
### Stwórz bazę danych
``` docker-compose exec users python manage.py recreate_db ```
### Zapełnij bazę danymi
``` docker-compose exec users python manage.py seed_db ```
### Uruchom testy
``` docker-compose exec users python manage.py test ```
