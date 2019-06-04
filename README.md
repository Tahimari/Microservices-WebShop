# Microservices-WebShop

## To apply model to dev database

```
docker-compose exec users python manage.py recreate_db
```

## To seed database
```
docker-compose exec users python manage.py seed_db
```

## To run app
```
docker-compose up -d --build
```

## To run users tests
```
docker-compose exec users python manage.py test
```
