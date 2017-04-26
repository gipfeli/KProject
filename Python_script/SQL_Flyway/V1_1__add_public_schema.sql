create table adressebuch
(
	adresse_id serial not null
		constraint adressebuch_pkey
			primary key,
	adresse_typ smallint
		constraint adressebuch_adresse_typ_fkey
			references referenzen.tbl_adresse_typ (id),
	adresse text,
	postfach text,
	plz char(4),
	ort text,
	land char(7),
	tel_1 char(18),
	email varchar(50)
)
;

create table patient
(
	patient_id serial not null
		constraint patient_id_pkey
			primary key,
	vorname varchar(35),
	nachname varchar(35),
	geschlecht smallint,
	geburtstag date,
	adresse_id integer not null
		constraint patient_id_contact_id_fkey
			references adressebuch,
	kk_nummer char(20) not null
		constraint patient_id_kk_nummer_key
			unique,
	ahv_nummer char(13)
)
;

