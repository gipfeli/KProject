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

Then use the `flyway migrate` (Check the flyway.conf first), to create the schemas and insert basic infromation (Swiss Insurance companies, Tessiner Code/ICD-10, PLZ, etc.)

Then running `XMLParser.py`(with HIN Client runnning in background), and type the card number in.

## TODO

- Add medicine list
- Add TARMED dataset
