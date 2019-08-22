# Microservices-WebShop

App is available on: <br>
http://3.120.148.31/

[![Build Status](https://travis-ci.com/Tahimari/Microservices-WebShop.svg?branch=master)](https://travis-ci.com/Tahimari/Microservices-WebShop)

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
