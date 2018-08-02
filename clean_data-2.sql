SET SQL_SAFE_UPDATES = 0;

truncate BMTRS.ADMINN;
truncate BMTRS.EXHIBIT;
truncate BMTRS.TICKET;
truncate BMTRS.REVIEW;
truncate BMTRS.CURATOR_REQUEST;
delete from BMTRS.MUSEUM;
delete from BMTRS.VISITOR;

INSERT INTO BMTRS.ADMINN VALUES ('alex@gatech.edu', 'iamadmin');
 
INSERT INTO BMTRS.VISITOR VALUES ('daniel@gatech.edu', 'bilingual', 1234567812345670,  1,  2020, 123);
INSERT INTO BMTRS.VISITOR VALUES ('helen@gatech.edu', 'architecture4ever', 8765432187654320,  2,  2021, 456);
INSERT INTO BMTRS.VISITOR VALUES ('zoe@gatech.edu', 'yogasister', 2468135924681350,  3,  2022, 789);
 
INSERT INTO BMTRS.MUSEUM VALUES ('MACBA', 'zoe@gatech.edu');
INSERT INTO BMTRS.MUSEUM VALUES ('Picasso Museum', NULL);
INSERT INTO BMTRS.MUSEUM VALUES ('CCCB', 'helen@gatech.edu');
 
INSERT INTO BMTRS.EXHIBIT VALUES ('MACBA', 'Bird', 2018, 'www.macba.es/bird/');
INSERT INTO BMTRS.EXHIBIT VALUES ('MACBA', 'Plane', 2018, 'www.macba.es/plane/');
INSERT INTO BMTRS.EXHIBIT VALUES ('MACBA', 'Train', 2018, 'www.macba.es/train/');
INSERT INTO BMTRS.EXHIBIT VALUES ('Picasso Museum', 'Geometric Shapes', 1900, 'www.picassomuseo.com/geo/');
INSERT INTO BMTRS.EXHIBIT VALUES ('CCCB', 'Black Light 1', 1985, 'www.cccb.com/bl1');
INSERT INTO BMTRS.EXHIBIT VALUES ('CCCB', 'Black Light 2', 1986, 'www.cccb.com/bl2');

INSERT INTO BMTRS.TICKET VALUES ('zoe@gatech.edu', 'MACBA', 5, '2018-05-20 00:00:00');
INSERT INTO BMTRS.TICKET VALUES ('helen@gatech.edu', 'Picasso Museum', 20, '2018-06-11 00:00:00');
INSERT INTO BMTRS.TICKET VALUES ('helen@gatech.edu', 'CCCB', 50, '2018-06-29 00:00:00');

INSERT INTO BMTRS.REVIEW VALUES ('zoe@gatech.edu', 'MACBA', 'Didnt get it.', 1);
INSERT INTO BMTRS.REVIEW VALUES ('helen@gatech.edu', 'Picasso Museum', 'So many shapes!', 5);
INSERT INTO BMTRS.REVIEW VALUES ('helen@gatech.edu', 'CCCB', 'Scary, but cool', 3);

INSERT INTO BMTRS.CURATOR_REQUEST VALUES ('zoe@gatech.edu', 'Picasso Museum');

SET SQL_SAFE_UPDATES = 1;