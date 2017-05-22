# KProjekt

A small medical application (card record system) for doctor's office

## Features

- Reading insurance number from cards, and fetching data from [HIN](https://www.hin.ch) (Subscription required).
- Adding patient's info in local Postgres database
- Using medicine list from Federal Office of Public Health Switzerland [(BaG)](https://www.bag.admin.ch/bag/en/home.html), directly through [outlet here](http://bag.e-mediat.net/SL2007.Web.External/ShowPreparations.aspx), to get tarif, price and instructions.

## Updates

- Add Pharmacode support. (Since 1.1.2015, BaG stopped include Pharmacode in their publications. However, some insurance systems hasn't updated/converted the system to use GTIN or Swissmedic-NR., there is still a need for Pharmacode)

## Creating Your Database

First, install [Flyway by BoxFuse](https://flywaydb.org). 

Then use the `flyway migrate` (Check the flyway.conf first), to create the schemas and insert basic infromation (Swiss Insurance companies, Tessiner Code/ICD-10, PLZ, TARMED, Medicine list (updated 27. April 2017) etc.)

Note: TARMED-List is now stored under tbl_leistung (german only). In case you want other language (italian or french), you can contact me at: [dat(at)gipfeli.info](mailto:dat@gipfeli.info)

## Using the software
0. Before running the scripts, add a `database.ini` file with correct database connection info in same folder.

```
[postgresql]
host=hostname
database=dbname
user=username
password=password
port=5432
```
1.1. `XMLParser.py`(with HIN Client runnning in background), and type the card number in. That would retrieve patient info from HIN, and insert it into database

1.2 `AutoUpdateMedListe.py` will automatically retrieve the Excel file from Federal Office of Public Health, or BaG, and insert data in database (Description, introduced date, SwissmedicNr, GTIN, and selling price).

1.3 (optional) `Add_pharma_code.py` will read the old publication of BaG (Jan.2015), compare the Swissmedic.Nr and add the pharmacode accordingly into the database. 



## TODO

- New columns in table bhlg_details (Behandlungsdetails), contains "receipt" (which'd contain med_id and quantity and date)
- Manual create bills (orange sheet) according to DiePost standard.

