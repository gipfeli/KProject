CREATE TABLE "referenzen".tbl_medlist
(
    id SERIAL PRIMARY KEY,
    bezeichnung TEXT,
    einf_datum DATE,
    swissmedic_nr CHAR(8),
    GTIN CHAR(13),
    preis NUMERIC(6,2)
);
CREATE INDEX table_name_id_index ON "referenzen".tbl_medlist (id);