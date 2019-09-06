# Microservices-WebShop

App is available on: <br>
http://3.120.148.31/

[![Build Status](https://travis-ci.com/Tahimari/Microservices-WebShop.svg?branch=master)](https://travis-ci.com/Tahimari/Microservices-WebShop)

Tematem tego projektu jest implementacja sklepu internetowego. Sklep pozwala na stworzenie konta użytkownika, zalogwanie się do systemu, przeglądanie oraz zakup produktu. Administrator ma możliwośc dodania, edycji oraz usunięcia prodktu. Aplikacje oferuje możliwość kontaktu poprzez formularz na stronie. Dodatkowo zadbano o resposynswność strony oraz skalowalność aplikacji. System Został wykonany w oparciu o architekture mikroserwisową. Frontend został stworzony w oparciu o framework Vue. Natomiast Backend powstał z użyciem frameworka flask. 4 serwisy odpowidają za moduł użytkowików, produktów, zamówień i dostaw. Część serwerowa korzysta z baz danych Sqlite oraz postgres w przypadku serwisu użytkowników. Aplikacja działa w środowisku docker, jest budowana za pomocą docker-compose. Strona została uruchomiona w chmurze obliczoniowej Amazon EC2, natomiast zdjęcia produktów są dynamicznie przechowywane w serwisie Amazon S3. Autoryzacja użytkowników odbywa się za pomocą tokena JWT generowanego w serwise użytkowników, i przychowywanym w localstorage przeglądarki.

## Run npm install
```
npm install front-service-vue
```

## To run app
```
docker-compose up -d --build
```

## To apply model to dev database
```
docker-compose exec users python manage.py recreate_db
```

## To seed database
```
docker-compose exec users python manage.py seed_db
```

## To run users tests
```
docker-compose exec users python manage.py test
```
