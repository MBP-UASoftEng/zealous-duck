BEGIN;
CREATE TABLE "product_product" ("id" serial NOT NULL PRIMARY KEY, "description" varchar(200) NOT NULL, "lookupcode" 
integer NOT NULL, "price" numeric(9, 2) NOT NULL, "itemType" smallint NOT NULL CHECK ("itemType" >= 0), "cost" 
numeric(9, 2) NOT NULL, "quantity" integer NOT NULL, "reorderPoint" integer NOT NULL, "restockLevel" integer NOT 
NULL, "extendedDescription" text NOT NULL, "active" boolean NOT NULL, "msrp" numeric(9, 2) NOT NULL, "dateCreated" 
date NOT NULL, "parentItem_id" integer NOT NULL);
ALTER TABLE "product_product" ADD CONSTRAINT "product_pr_parentItem_id_69baa001fc867361_fk_product_product_id" 
FOREIGN KEY ("parentItem_id") REFERENCES "product_product" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "product_product_6d0255a6" ON "product_product" ("parentItem_id");

COMMIT;
