create sequence tbl_adresse_typ_id_seq
;

create sequence tbl_geschlecht_id_seq
;

create sequence tbl_gesetz_id_seq
;

create sequence tbl_plz_id_seq
;

create sequence tbl_ti_code_id_seq
;

create sequence tbl_versicher_contact_id_seq
;

create sequence tbl_versicher_id_seq
;

create table referenzen.tbl_adresse_typ
(
  id serial not null
    constraint tbl_adresse_typ_pkey
      primary key,
  typ varchar(15)
)
;

create table referenzen.tbl_geschlecht
(
  id serial not null
    constraint tbl_geschlecht_pkey
      primary key,
  geschlecht text
)
;

create table referenzen.tbl_gesetz
(
  id serial not null
    constraint tbl_gesetz_pkey
      primary key,
  gesetz char(3)
)
;

create table referenzen.tbl_plz
(
  id serial not null
    constraint tbl_plz_pkey
      primary key,
  plz char(4),
  ortsname varchar(40)
)
;

create table referenzen.tbl_ti_code
(
  id serial not null
    constraint tbl_ti_code_pkey
      primary key,
  typ varchar(5),
  code char(2) not null
    constraint tbl_ti_code_code_key
      unique,
  bezeichnung text
)
;

create table referenzen.tbl_versicher
(
  id serial not null
    constraint tbl_versicher_pkey
      primary key,
  kk_name text not null,
  kk_dept text,
  xml_kk_name text not null,
  "insuranceGLN" char(13),
  "recepientGLN" char(13),
  gesetz_code smallint
    constraint tbl_versicher_gesetz_code_fkey
      references referenzen.tbl_gesetz,
  tp_elektronisch boolean default true,
  adresse_id serial
)
;

