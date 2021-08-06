### Описание
Несложный REST API на тематику продаж машин дилерами, реализованный с помощью Django REST framework. 
Реализован только бэкенд, хотя данный фреймворк генерирует простенький графический интерфейс.
Все модели данных (Car, Dealer, Sale) описаны в файле cars_sellings/models.py при помощи Django ORM.
Здесь даны краткие описания полей:

#### Car
* year - год изготовления машины, неотрицательное целое число
* model - модель машины, текстовое поле
* manufacturer - производитель машины, текстовое поле
* color - цвет машины, текстовое поле
* mileage - пробег, неотрицательное целое число
 
#### Dealer
* name - название / имя дилера, текстовое поле

#### Sale
* price - цена, за которую машина была продана, неотрицательное целое число
* car - внешний ключ на машину, которая была продана
* dealer - внешний ключ на дилера, который продал машину

В качестве описания эндпоинтов и формата JSON приведена спецификация OpenAPI (файл car_sales_OpenAPI_spec.yml)

### Установка
```pip install -r requirements.txt```

### Запуск
Из корня проекта запустить ```python manage.py runserver```

### Примеры запросов
Для краткости приведены сами запросы (с помощью утилиты curl), HTTP-код ответа и данные JSON для модели cars. С остальными моделями работа ничем не отличается.

### POST
```
curl -v http://127.0.0.1:8000/cars/ -H "Content-type:application/json" -X POST -d @json_msg1.txt

< HTTP/1.1 201 Created

{"id":5,"year":1999,"model":"Car Test Model 1","manufacturer":"Cool Motors Inc","color":"Green","mileage":0}
```

Файл json_msg1.txt:
```
{
	"year": 1999, 
	"model": "Car Test Model 1", 
	"manufacturer": "Cool Motors Inc", 
	"color": "Green", 
	"mileage": 0
}
```

#### GET
```
curl -v http://127.0.0.1:8000/cars/

< HTTP/1.1 200 OK

{"id":1,"year":2011,"model":"Polo","manufacturer":"Volkswagen","color":"Black","mileage":89000},
{"id":2,"year":1999,"model":"Car Test Model 1","manufacturer":"Cool Motors Inc","color":"Green","mileage":0}
```

#### DELETE
```
curl -v http://127.0.0.1:8000/cars/2/ -X DELETE

< HTTP/1.1 204 No Content
```

#### PUT
```
curl -v http://127.0.0.1:8000/cars/5/ -H "Content-type:application/json" -X PUT -d @json_msg2.txt

< HTTP/1.1 200 OK

{"id":5,"year":2017,"model":"Some Another Model","manufacturer":"Yeah Boi Motors","color":"Black","mileage":55000}*
```

#### PATCH 
```
curl -v http://127.0.0.1:8000/cars/5/ -H "Content-type:application/json" -X PATCH -d "{\"model\":\"Patched Model\"}"

< HTTP/1.1 200 OK

{"id":5,"year":2017,"model":"Patched Model","manufacturer":"Yeah Boi Motors","color":"Black","mileage":55000}
```

### 

