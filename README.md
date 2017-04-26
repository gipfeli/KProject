# KProjekt

A small medical application (card record system) for doctor's office

## Features

- Reading insurance number from cards, and fetching data from [HIN](https://www.hin.ch) (Subscription required).
- Adding patient's info in local Postgres database
- Using medicine list from Federal Office of Public Health Switzerland [(BaG)](https://www.bag.admin.ch/bag/en/home.html), directly through [outlet here](http://bag.e-mediat.net/SL2007.Web.External/ShowPreparations.aspx), to get tarif, price and instructions.

## How to Use

Please wait for a bit more...

## Creating Your Database

First, install [Flyway by BoxFuse](https://flywaydb.org). 

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
