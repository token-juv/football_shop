# My first Django project
## Online store - _**football_shop**_

---

### Versions

* **Python version** - 3.12+
* **Django verison** - 4.2+
* **PostgreSQL** - 16

---

#### Install PostreSQL

- Install PostgresSQL 16 and pgAdmin 4
- Create user store with password store
- Create table store with user store

---

#### Run

- Change directory to football_shop:

```
cd football_shop_project
```

- Create virtual environment:

```
python -m venv venv
```

- Activate virtual enviroment:

```
venv\Scripts\activate
```

- Install dependencies:

```
pip install requirements.txt

```

- Create migrations:
```
python manage.py makemigrations

python manage.py migrate
```

- Create superuser:

```
python manage.py createsuperuser
```

- Load fixtures:
```
python manage.py loaddata fixtures/product/categories.json
python manage.py loaddata fixtures/product/products.json  
```

- Run server:

```
python manage.py runserver
```

---
