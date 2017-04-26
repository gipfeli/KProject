create sequence behandlung_id_seq
;

create sequence bhlg_detail_id_seq
;

create sequence fall_fall_id_seq
;

create sequence fll_detail_id_seq
;

create table konsultation.behandlung
(
	id bigserial not null
		constraint behandlung_pkey
			primary key,
	fall_id integer not null,
	datum date default ('now'::text)::date,
	rechnung_id integer,
	rechnung_status smallint,
	betrag numeric(6,2)
)
;

create table konsultation.bhlg_detail
(
	id serial not null
		constraint bhlg_detail_pkey
			primary key,
	subjektiv text,
	objektiv text,
	"analyse" text,
	prozedere text,
	bhlg_id bigint
		constraint bhlg_detail_bhlg_id_fkey
			references konsultation.behandlung
)
;

create table konsultation.fall
(
	fall_id bigserial not null
		constraint fall_pkey
			primary key,
	betreff text,
	bhlg_typ_ist_krankheit boolean default true,
	verguetung_ist_tp boolean default true,
	gesetz smallint
		constraint fall_gesetz_fkey
			references referenzen.tbl_gesetz (id),
	patient_id integer,
	fll_geschlossen boolean default false
)
;

alter table konsultation.behandlung
	add constraint behandlung_fall_id_fkey
		foreign key (fall_id) references konsultation.fall
;

create table konsultation.fll_detail
(
	id serial not null
		constraint fll_detail_pkey
			primary key,
	verguetung_id varchar(35),
	vertrag_id varchar(35),
	arbeitsgeber_nr varchar(35),
	anzahl_bhlg smallint,
	fall_id integer
		constraint fll_detail_fall_id_fkey
			references konsultation.fall
)
;

