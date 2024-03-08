INSERT INTO angajati VALUES(1, 'Popescu', 'Alexandra', 'administrator', TO_DATE('02-01-2020', 'DD-MM-YYYY'), 24000);
INSERT INTO angajati VALUES(2, 'Ionescu', 'Mihai', 'angajat_casa', TO_DATE('06-03-2023', 'DD-MM-YYYY'), 3000);
INSERT INTO angajati VALUES(3, 'Dumitrescu', 'Elena', 'angajat_marfa', TO_DATE('15-04-2020', 'DD-MM-YYYY'), 3000);
INSERT INTO angajati VALUES(4, 'Radu', 'Gabriel', 'livrator', TO_DATE('04-01-2020', 'DD-MM-YYYY'), 8000);
INSERT INTO angajati VALUES(5, 'Cojocaru', 'Ana', 'livrator', TO_DATE('02-09-2020', 'DD-MM-YYYY'), 5000);
select * from angajati;

insert into client (nume_client) values ('Ion');
insert into client (nume_client) values ('Bogdan');
insert into client (nume_client) values ('Alex');
insert into client (nume_client) values ('Sorin');
insert into client (nume_client) values ('Andra');

select * from client;

insert into detalii_client values (1, 3, 'iasi iasi', to_date('08-11-1984', 'dd-mm-yyyy'), 'F',  'a1@b1.co');
insert into detalii_client values (2, 4, 'bacau bacau', to_date('12-03-1981', 'dd-mm-yyyy'), 'M',  'afdsf1@b1.co');
insert into detalii_client values (3, 2, 'iasi letcani', to_date('06-07-1983', 'dd-mm-yyyy'), 'M',  'dgff1@b1.co');
insert into detalii_client values (4, 5, 'bucuresti bucuresti', to_date('08-11-1984', 'dd-mm-yyyy'), 'M',  'dgff1@b1.com');
insert into detalii_client values (5, 6, 'Brasov Brasov', to_date('22-09-1994', 'dd-mm-yyyy'), 'M',  'dgdsfsdgf1@b1.com');

select * from detalii_client;

insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('02-01-2024', 'dd-mm-yyyy'), 2, 3);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('02-01-2024', 'dd-mm-yyyy'), 3, 4);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('03-01-2024', 'dd-mm-yyyy'), 2, 2);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('05-01-2024', 'dd-mm-yyyy'), 2, 3);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('04-01-2024', 'dd-mm-yyyy'), 2, 3);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('02-01-2024', 'dd-mm-yyyy'), 3, 5);
insert into comanda (data_comanda, angajati_id_angajat, client_id_client) values (to_date('01-01-2024', 'dd-mm-yyyy'), 2, 6);


select * from comanda;


INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (1, 'Pelikan', '0752517294');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (2, 'Dixon', '0744494812');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (3, 'BIC', '0742149754');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (4, 'LIBRIS', '0796530212');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (5, 'DELI', '0706396412');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (6, 'BOOKZONE', '0786401256');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (7, 'NIKE', '0747921021');
INSERT INTO furnizor (id_furnizor, nume_furnizor, telefon_furnizor)
VALUES (8, 'POSCA', '0742348712');

select * from furnizor;

insert into produse values (1, 'penar', 7, 20, 1);
insert into produse values (2, 'caiet', 13, 45, 3);
insert into produse values (3, 'abecedar', 22, 84, 4);
insert into produse values (4, 'pix', 8, 20, 6);
insert into produse values (5, 'stilou', 3, 100, 7);
insert into produse values (6, 'geanta', 39, 16, 2);
insert into produse values (7, 'acuarele', 27, 2, 6);

select * from produse;


insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (2, 4, 2);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (1, 4, 2);

insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (2, 5, 1);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (6, 5, 3);

insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (2, 6, 1);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (3, 6, 3);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (5, 6, 5);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (1, 6, 1);

insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (4, 7, 5);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (5, 7, 1);

insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (4, 9, 5);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (5, 9, 1);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (6, 9, 2);


insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (3, 8, 5);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (5, 8, 3);

insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (3, 10, 5);
insert into relation_prod_com (produse_id_produs, comanda_id_comanda, cantitate) values (6, 10, 3);

select * from comanda;

select * from detalii_client;
