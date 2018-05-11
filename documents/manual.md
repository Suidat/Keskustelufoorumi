# Asennus

Lataa repositorio, ja lataa riippuvuudet komennolla "pip install -r requirements.txt".
Tämän jälkeen voidaan sovellus käynnistää komennolla "python ./run.py".
Tarkista terminaalista sovelluksen osoite, ja mene osoitteeseen haluamallasi selaimella.


# Käyttöohje

Sovelluksen käyttämiseen tarvitaan käyttäjätunnukset. Ne voidaan luoda joko valitsemalla ylhäältä oikealta "Sign Up"-linkki, tai menemällä sovelluksen osoitteesseen "/user/new". Lomakkeeseen syötetään haluttu käyttäjätunnus ja salasana. Jos käyttäjätunnus on varattu ilmoitetaan asiasta, ja käyttäjä joutuu valitsemaan uuden tunnuksen.

Tämän jälkeen voidaan sovellukseen kirjautua sisään joko linkistä "Login", joka löytyy "Sign Up"-linkin vierestä, tai osoitteesta "/user/login". Lomakkeeseen syötetään tunnukset, jonka jälkeen käyttäjä ohjataan omille sivuilleen, joilla näytettän tiedot siitä, mitkä ryhmät ja keskustelut ovat hänen luomiaan. Täältä voidaan myös vaihtaa käyttäjän salasanaa, sekä hallinoida ryhmiä ja keskusteluja.

Painamalla yläpalkissa olevaa Keskustelupalasta linkkiä, voidaan siirtyä ryhmien listaukseen, missä kirjautunut käyttäjä voi luoda uusia ryhmiä ja kaikki käyttäjät voivat tarkastella jo luotuja ryhmiä. Ryhmän luonti onnistuu painamalla "Create new group"-linkkiä ja syöttämällä ryhmän nimen tekstikenttään. Ryhmien sisältöä voidaan tarkastella valitsemalla ryhmän nimi.

Ryhmässä voidaan lukea keskustelujen aiheet, ja nähdään kaikki ryhmässä olevat käyttäjät. Jotta ryhmässä voidaan tehdä jotain, täytyy ryhmään liittyä. Jos olet luonut ryhmän kirjataan sinut automaattisesti ryhmän jäseneksi. Ryhmän luoja voi halutessaan estää tiettyjä käyttäjiä käyttämästä ryhmää painamalla nimen vieressä olevaa "Ban user"-linkkiä. Tämä estää kyseistä käyttäjää tekemästä kyseisessä ryhmässä mitään.

Keskustelu luodaan kuten ryhmäkin, painamalla ryhmässä linkkiä "Create new discussion", ja syöttämllä haluttu aihe kenttään. Tämän jälkeen voidaan keskusteluun syöttää viestejä tekstikentästä ja painamalla "Post message" nappia. Viestin lähettäjä ja ryhmän omistaja voivat halutessaan poistaa viestejä, tai muokata niiden sisältöä. Ryhmän omistaja voi muokata/poistaa kaikkia ryhmän viestejä, mutta lähettäjä voi muokata/poistaa ainoastaan omiaan.
