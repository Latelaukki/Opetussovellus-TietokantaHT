# Opetussovellus-TietokantaHT

Tämän sovelluksen tarkoituksena on tarjota yksinkertainen alusta opetuskursseille ja toimia SQL-websovellus-harjoituksena. 

Sovelluksessa on kolme eri käyttäjätyyppiä ja niiden alustavat oikeudet toiminnallisuuksiin: 
* Opiskelija - voi luoda tunnuksen, ilmoittautua kursseille ja ratkoa tehtäviä
* Opettaja - voi seurata opiskelijoiden edistymistä
* Ylläpitäjä - voi lisätä kursseja ja niille materiaalia, poistaa käyttäjiä ja muut ilmenevät hallinnolliset oikeudet

Lisäksi kursseille voi lisätä tekstimateriaalia ja monivalintatehtäviä. Tehtävät voi tarkistaa automaattisesti.

Sovellukseen pääsee [täältä](https://tietokanta-opetussovellus.herokuapp.com/):

Sovelluksen tila tällä hetkellä:

Sovelluksen voi avata, mutta itselleni aukeaa vain uloskirjautumislinkki. Tunnuksen luonti pitäisi toimia, mutta uloskirjautuminen puuttuu, joten kerran sisään kirjauduttua register-sivulle ei ilmeisesti pääse. Kurssien käsittely on vielä kokonaan toteuttamatta, courses-taulu on kuitenkin luotu tietokantaan. 

Sisäänkirjautuminen aiheuttaa oudon varoituksen tietosuojaloukkauksesta. Ei vielä ihan selvinnyt, mitä tarkoittaa.

Schema.sql ei päivittynyt herokuun, users-taulun attribuutit ovat väärät. Lieneekö syy, että samanniminen taulu pitää ensin poistaa tietokannasta(?). Korjaus ei ehdi tähän palautukseen.


