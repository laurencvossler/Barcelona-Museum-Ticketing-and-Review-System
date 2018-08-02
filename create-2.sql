CREATE TABLE BMTRS.ADMINN (
	email VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100) NOT NULL
);

 CREATE TABLE BMTRS.VISITOR (
 	email VARCHAR(100) PRIMARY KEY,
     password VARCHAR(100) NOT NULL,
     credit_card_num CHAR(16) NOT NULL,
     expiration_month INTEGER NOT NULL,
     expiration_year CHAR(4) NOT NULL,
     credit_card_security_num INTEGER NOT NULL
);

CREATE TABLE BMTRS.MUSEUM (
 	 museum_name VARCHAR(100) PRIMARY KEY,
     curator_email VARCHAR(100),
     FOREIGN KEY (curator_email) REFERENCES VISITOR(email)
);
--
CREATE TABLE BMTRS.CURATOR_REQUEST (
	email VARCHAR(100) NOT NULL,
    museum_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (email) REFERENCES VISITOR(email) ON DELETE CASCADE,
    FOREIGN KEY (museum_name) REFERENCES MUSEUM(museum_name) ON DELETE CASCADE,
    PRIMARY KEY (email, museum_name)
);

CREATE TABLE BMTRS.REVIEW (
	email VARCHAR(100) NOT NULL,
	museum_name VARCHAR(100) NOT NULL,
	comment VARCHAR(100),
	rating INTEGER NOT NULL,
	PRIMARY KEY (email, museum_name),
	FOREIGN KEY (email) REFERENCES VISITOR(email) ON DELETE CASCADE,
	FOREIGN KEY (museum_name) REFERENCES MUSEUM(museum_name) ON DELETE CASCADE
);

CREATE TABLE BMTRS.TICKET (
	email VARCHAR(100) NOT NULL,
	museum_name VARCHAR(100) NOT NULL,
    price VARCHAR(100),
    purchase_timestamp DATETIME,
    PRIMARY KEY (email, museum_name),
	FOREIGN KEY (email) REFERENCES VISITOR(email) ON DELETE CASCADE,
	FOREIGN KEY (museum_name) REFERENCES MUSEUM(museum_name) ON DELETE CASCADE
);

CREATE TABLE BMTRS.EXHIBIT (
	museum_name VARCHAR(100) NOT NULL,
    exhibit_name VARCHAR(100) NOT NULL,
    year INTEGER,
    url VARCHAR(100),
    PRIMARY KEY (museum_name, exhibit_name),
    FOREIGN KEY (museum_name) REFERENCES MUSEUM(museum_name) ON DELETE CASCADE
);

