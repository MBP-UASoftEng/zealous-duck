BEGIN;
CREATE TABLE "zealousduck_employee" ("id" serial NOT NULL PRIMARY KEY, "name_first" varchar(100) NOT NULL, 
"name_last" varchar(100) NOT NULL, "active" boolean NOT NULL, "type" smallint NOT NULL CHECK ("type" >= 0), 
"password" varchar(100) NOT NULL, "timestamp" date NOT NULL);
CREATE TABLE "zealousduck_product" ("id" serial NOT NULL PRIMARY KEY, "description" varchar(200) NOT NULL, 
"lookupcode" integer NOT NULL, "price" numeric(10, 2) NOT NULL, "itemType" smallint NOT NULL CHECK ("itemType" >= 
0), "cost" numeric(10, 2) NOT NULL, "quantity" integer NOT NULL, "reorderPoint" integer NOT NULL, "restockLevel" 
integer NOT NULL, "extendedDescription" text NOT NULL, "active" boolean NOT NULL, "msrp" numeric(10, 2) NOT NULL, 
"dateCreated" date NOT NULL, "parentItem_id" integer NOT NULL);
CREATE TABLE "zealousduck_tenderentry" ("id" serial NOT NULL PRIMARY KEY, "tenderType" smallint NOT NULL CHECK 
("tenderType" >= 0), "amount" numeric(10, 2) NOT NULL, "timestamp" timestamp with time zone NOT NULL);
CREATE TABLE "zealousduck_transaction" ("id" serial NOT NULL PRIMARY KEY, "amount" numeric(10, 2) NOT NULL, 
"transactionType" smallint NOT NULL CHECK ("transactionType" >= 0), "timestamp" timestamp with time zone NOT NULL, 
"cashierID_id" integer NOT NULL, "parent_id" integer NOT NULL);
CREATE TABLE "zealousduck_transactionentry" ("id" serial NOT NULL PRIMARY KEY, "price" numeric(10, 2) NOT NULL, 
"quantity" integer NOT NULL, "productID_id" integer NOT NULL, "transactionID_id" integer NOT NULL);
ALTER TABLE "zealousduck_tenderentry" ADD COLUMN "transactionID_id" integer NOT NULL;
ALTER TABLE "zealousduck_tenderentry" ALTER COLUMN "transactionID_id" DROP DEFAULT;
ALTER TABLE "zealousduck_product" ADD CONSTRAINT "zealou_parentItem_id_525233cae83a8a06_fk_zealousduck_product_id" 
FOREIGN KEY ("parentItem_id") REFERENCES "zealousduck_product" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "zealousduck_product_6d0255a6" ON "zealousduck_product" ("parentItem_id");
ALTER TABLE "zealousduck_transaction" ADD CONSTRAINT 
"zealou_cashierID_id_5bc6e49db5208905_fk_zealousduck_employee_id" FOREIGN KEY ("cashierID_id") REFERENCES 
"zealousduck_employee" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "zealousduck_transaction" ADD CONSTRAINT 
"zealous_parent_id_573e1cf7e37abc2_fk_zealousduck_transaction_id" FOREIGN KEY ("parent_id") REFERENCES 
"zealousduck_transaction" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "zealousduck_transaction_9f590698" ON "zealousduck_transaction" ("cashierID_id");
CREATE INDEX "zealousduck_transaction_6be37982" ON "zealousduck_transaction" ("parent_id");
ALTER TABLE "zealousduck_transactionentry" ADD CONSTRAINT 
"zealous_productID_id_195c0444cb30bf9a_fk_zealousduck_product_id" FOREIGN KEY ("productID_id") REFERENCES 
"zealousduck_product" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "zealousduck_transactionentry" ADD CONSTRAINT "D5bf56f2bbafb174f55fd853b4af61e8" FOREIGN KEY 
("transactionID_id") REFERENCES "zealousduck_transaction" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "zealousduck_transactionentry_95a10fc8" ON "zealousduck_transactionentry" ("productID_id");
CREATE INDEX "zealousduck_transactionentry_eef209d9" ON "zealousduck_transactionentry" ("transactionID_id");
CREATE INDEX "zealousduck_tenderentry_eef209d9" ON "zealousduck_tenderentry" ("transactionID_id");
ALTER TABLE "zealousduck_tenderentry" ADD CONSTRAINT "D783954b7cc767530ac22efc3bdd6702" FOREIGN KEY 
("transactionID_id") REFERENCES "zealousduck_transaction" ("id") DEFERRABLE INITIALLY DEFERRED;

COMMIT;

