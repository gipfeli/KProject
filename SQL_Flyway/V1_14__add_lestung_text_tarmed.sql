create table referenzen.tbl_leistung
(
	id serial not null
		constraint tbl_leistung_pkey
			primary key,
	lnr varchar(8),
	bez_255 text,
	med_interpret text,
	tech_interpret text,
	gueltig_von date,
	gueltig_bis date,
	mut_dat date
)
;

