# Opetussovellus-TietokantaHT

Tämän sovelluksen tarkoituksena on tarjota yksinkertainen alusta opetuskursseille ja toimia SQL-websovellus-harjoituksena. 

Sovelluksessa on kolme eri käyttäjätyyppiä ja niiden alustavat oikeudet toiminnallisuuksiin: 
* Opiskelija - voi luoda tunnuksen, tarkastella omaa profiiliaan, ilmoittautua kursseille ja ratkoa tehtäviä
* Opettaja - voi tarkastella kursseille ilmoittautuneita opiskelijoita sekä heidän edistymistään ja lisätä kursseja ja materiaaleja ja mahdollisesti lisätä muita opettajia
* Ylläpitäjä - voi tarkastella ja poistaa muita käyttäjiä ja jakaa tai poistaa käyttöoikeuksia
  
Lisäksi kursseille voi lisätä tekstimateriaalia ja monivalintatehtäviä.

Sovellukseen pääsee [täältä](https://tietokanta-opetussovellus.herokuapp.com/):


## Sovelluksen lopputulos

Ylläolevan kuvailun ominaisuudet toteutuivat lukuunottamatta kurssitehtävien ratkaisemista. Kurssin opettaja pystyy kuitenkin tekemään tehtäviä ja merkitsemään oikeat vastaukset ja oppilaat pääsevät tarkastelemaan tehtäviä, mutta eivät ratkaisemaan.

Lisäksi ulkomuotoilu jäi kolkoksi, sillä aikaa ei jäänyt tyylin säätämiseen.

## Käyttöohjeet

Sovellukseen pääse yllä olevasta linkistä. Alkuikkunasta pääsee kirjautumaan seuraavilla tunnuksilla:

käyttäjätunnus: ```admin001```

salasana: ```testiadmin```

Tunnuksella on ylläpitäjän oikeudet. Ylläpitäjänä voi lisätä itsensä opettajaksi, jolloin voi tarkastella sivuja opettajan oikeuksilla. Ylläpitäjänä pystyy tarkastelemaan muita käyttäjiä "selaa profiileja" linkistä, josta pääsee lisäämään oikeuksia ja poistamaan käyttäjän. HUOM! Opettaja-käyttäjää ei voi poistaa, sillä se vaikuttaisi olemassa oleviin kursseihin. Muut käyttäjät voi poistaa, myös ylläpitäjä-käyttäjän.

"Selaa kursseja", pääsee tarkastelemaan luotuja kursseja. Kurssi koodien tulee olla erilaisia, mutta nimet voivat olla samoja. Tällä hetkelllä kursseilla on vain yksi vastuuopettaja, joka muodostuu automaattisesti, kun opettaja luo kurssin. Opettajien lisääminen kursseille ei sinänsä olisi monimutkaista toteuttaa, mutta aika loppui kesken.

Tehtäviä pystyy luomaan max 4, sillä en keksinyt miten saisin iteroitua kysymyksiä ja niiden vaihtoehtoja järkevästi. Tehtävistä ei ole kuitenkaan hirveästi iloa, sillä niitä ei pysty ratkaisemaan.
