Tietorakenteita on viisi ja yksi abstrakti luokka, johon kaikki muut tietorakenteet perustuvat. Tietorakenteita ovat Account, Groups, Discussion, Message ja liitostauluna Accountin ja Groupsin välillä toimii Linkag, jossa on myös tieto siitä, onko käyttäjä bannitty.

Tietokantataulut ja tietokannat vastaavat täysin toisiaan. Tiettyjä vaatimuksia, kuten esim Account luokan UNIQUE(name) vaatimuksia ei ole lisätty Tietokantatauluun.




CREATE TABLE-lauseet:

``` SQL
CREATE TABLE "Account" (

	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	password VARCHAR(200) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (name)
);

CREATE TABLE "Groups" (

	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	owner_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(owner_id) REFERENCES "Account" (id)
);
CREATE TABLE "Discussion" (

	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	group_id INTEGER NOT NULL,
	owner_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(group_id) REFERENCES "Groups" (id),
	FOREIGN KEY(owner_id) REFERENCES "Account" (id)
);
CREATE TABLE "Linkag" (

	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	group_id INTEGER NOT NULL,
	account_id INTEGER NOT NULL,
	banned BOOLEAN NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(group_id) REFERENCES "Groups" (id),
	FOREIGN KEY(account_id) REFERENCES "Account" (id),
	CHECK (banned IN (0, 1))
);
CREATE TABLE "Message" (

	id INTEGER NOT NULL,
	date_created DATETIME,
	date_modified DATETIME,
	message TEXT NOT NULL,
	discussion_id INTEGER NOT NULL,
	sender_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(discussion_id) REFERENCES "Discussion" (id),
	FOREIGN KEY(sender_id) REFERENCES "Account" (id)
);
```
