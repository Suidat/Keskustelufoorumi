User Story | Status|SQL
---|---|---
As a user I want to be able to change my account details | Done| UPDATE Account SET password = :password WHERE id = :user
As a user I want to be able to sign up| Done |
As a user I want to be able to login| Done |
As a user I want to be able to post messages| Done |
As a user I want to be able to start a new group| Done |
As a user I want to be able to start a new discussion| Done |
As a user I want to be able to post a message in an existing discussion| Done |
As a user I want to be able to modify my old messages| Done |UPDATE Message SET message = :edit WHERE id = :id
As a user I want to be able to delete my old messages| Done |DELETE FROM Message WHERE id = :id
as a user I want messages to be paged | Done | SELECT Account.name AS username, Message.* FROM Account, Message WHERE Account.id=Message.sender_id AND Message.discussion_id = :disc ORDER BY Message.date_created ASC LIMIT 10 OFFSET :page
As a user I want to be able to join groups| Done |
As an administrator I want to be able to ban users| Done |
As an administrator I want to be able to add new users to my group/s | REMOVED
As an administrator I want to be able to remove messages| Done | DELETE FROM Message WHERE id = :id
As an administrator I want to be able to remove users from my group/s | Changed to banning|


Joihinkin User storyhin liittyvät SQL-kyselyt onnistuivat simppelillä haulla, ja niitä ei ole listattu. Tässä on joitain SQL-kyselyitä, joille ei ole sopivaa user storyä:

Haetaan Group tiedot, ja sen omistavan käyttäjän nimi
``` SQL
SELECT Groups.*, Account.name as username From Groups, Account WHERE Groups.owner_id = Account.id AND Account.id = :id
```
Haetaan käyttäjän kaikki keskustelut ja niihin kuuluvien viestien määrä
```SQL
SELECT Discussion.*, Account.id as user_id, COUNT(Message.id) AS amount FROM Account, Discussion LEFT OUTER JOIN Message ON Discussion.id = Message.discussion_id WHERE Discussion.owner_id = Account.id AND Account.id = :id GROUP BY Discussion.id
```
Haetaan ryhmään kuuluvien käyttäjien nimet ja ovatko he estettyjä
``` SQL
SELECT Account.id, Account.name As username, Linkag.group_id, Linkag.banned FROM Account, Linkag Where Linkag.account_id = Account.id AND Linkag.group_id = :id
```
