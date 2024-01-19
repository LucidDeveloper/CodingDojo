-- Query: Create 3 new dojos
INSERT INTO dojos(name,created_at,updated_at) VALUES('Supreme Dojo', NOW(), NOW());
INSERT INTO dojos(name,created_at,updated_at) VALUES('Extreme Dojo', NOW(), NOW());
INSERT INTO dojos(name,created_at,updated_at) VALUES('Supremely Extreme Dojo', NOW(), NOW());
SELECT * FROM dojos;

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id <= 3;
SELECT * FROM dojos;

-- Query: Create 3 more dojos
INSERT INTO dojos(name,created_at,updated_at) VALUES('Supreme Dojo', NOW(), NOW());
INSERT INTO dojos(name,created_at,updated_at) VALUES('Extreme Dojo', NOW(), NOW());
INSERT INTO dojos(name,created_at,updated_at) VALUES('Supremely Extreme Dojo', NOW(), NOW());
SELECT * FROM dojos;

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Gianni', 'Javier', 32, NOW(), NOW(),4);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Reinaldo', 'Javier', 32, NOW(), NOW(),4);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Clara', 'Javier', 32, NOW(), NOW(),4);
SELECT * FROM ninjas;

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Andrea', 'Avila', 27, NOW(), NOW(),5);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Vi', 'Avila', 15, NOW(), NOW(),5);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('June', 'Avila', 7, NOW(), NOW(),5);
SELECT * FROM ninjas;

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Patrick', 'Javier', 25, NOW(), NOW(),6);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Antonius', 'Javier', 40, NOW(), NOW(),6);
INSERT INTO ninjas(first_name,last_name, age, created_at, updated_at, dojo_id) VALUES('Bruno', 'Javier', 30, NOW(), NOW(),6);
SELECT * FROM ninjas;

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo
SELECT dojos.name as dojo_name FROM dojos
JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;
