BEGIN TRANSACTION;
INSERT INTO "users" VALUES(3,'Alex');
SELECT * FROM "users";
ROLLBACK;
