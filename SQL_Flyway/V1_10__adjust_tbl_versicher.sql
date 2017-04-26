ALTER TABLE "referenzen"."tbl_versicher"
  ALTER COLUMN "adresse_id" DROP DEFAULT,
  ADD FOREIGN KEY ("adresse_id") REFERENCES "public"."adressebuch"("adresse_id");
