# Keskustelufoorumi

[Linkki sovelluksen sivulle](https://peaceful-plains-52396.herokuapp.com/)

[Linkki user storyhin](documents/user_stories.md)

[Linkki tietokantakaavioon](documents/tietokantakaavio.pdf)

[Linkki käyttö- ja asennusohjeisiin](documents/manual.md)

[Tietorakenteista](documents/tietorakenteet.md)


## Kuvaus

Sovellus on Keskustelufoorumi, jolla voidaan luoda ryhmiä, keskusteluja sekä viestejä keskusteluihin. Keskusteluissa käyttäjät voivat poistaa omia viestejään, tai muokata niiden sisältöä. Sovelluksessa ei ole yksittäistä käyttäjää, joka voi hallinnoida koko sovellusta, vaan jokaisen ryhmän omistaja voi tarvittaessa poistaa keskusteluja tai estää käyttäjiä toimimasta ryhmässä. Sovellus toimii Herokussa, mutta sitä voi myös käyttää locaalisti terminaalista.

## Omat kokemukset

- Herokun kanssa työskentely ei ole ollut ruusuilla tanssimista. Tietorakenteet eivät aina toimineet, joskus mikään ei toiminut, mutta koko ajan löytyi jotain korjattavaa tai muutettavaa.

- Aikataulutus ei ole ollut vahvasti mukana tässä projektissa enimmäkseen erillisten tapahtumien johdosta, joiden takia jouduin lykkäämään useammalla viikolla asioiden tekemistä. Siitä syystä suurimmat muutokset ovat tapahtuneet viimeisen parin viikon aikana.

## Rajoitteet

- Sovelluksessa ei voida poistaa ryhmiä tai keskusteluja. Näihin on metodit, mutta niitä ei voi kutsua muuten kuin terminaalin kautta. En katsonut niitä tarpeellisiksi harjoitustyön kannalta, kun poistaminen on muualla mahdollista.

- Käyttäjät eivät saa muuttaa nimiään.

- Johtuen omasta html taidosta, tai sen puutteesta, ovat sivut hyvin simppeleitä, mutta myös ehkä huonosti kirjoitettuja.

## Puutteet

- Sovelluksella ei voi kovin moni henkilö tehdä samanaikaisesti asioita, johtuen Herokusta.

- Sovelluksessa ei ole niin sanottua Adminia, vaan jokaisella ryhmällä on oma omistaja, joka hallinnoi kyseistä ryhmää.
  - Tätä voisi muuttaa, Account tietorakenteessa on jo mahdollisuus rooleille, mutta koska en katsonut sitä niin tarpeelliseksi, se ei tee mitään.

- Jokaista ryhmää voi hallinoida vain yksi henkilö, mutta tämän voisi vaihtaa, esim mahdollistamalla samanlaisen toiminnon kuin käyttäjän banniminen, mutta vain adminiksi teossa.

- Sovelluksen haku ominaisuus toimii hieman sovelluksen toimintaa vastaan, sillä sen avulla voi estetty käyttäjä nähdä kaikkien ryhmien sisäiset keskustelut. Tämän korjaaminen olisi työlästä, en ole edes keksinyt tapaa jolla toteuttaa tätä vielä.
