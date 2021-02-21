# Opetussovellus-TietokantaHT

Tämän sovelluksen tarkoituksena on tarjota yksinkertainen alusta opetuskursseille ja toimia SQL-websovellus-harjoituksena. 

Sovelluksessa on kolme eri käyttäjätyyppiä ja niiden alustavat oikeudet toiminnallisuuksiin: 
* Opiskelija - voi luoda tunnuksen, tarkastella omaa profiiliaan, ilmoittautua kursseille ja ratkoa tehtäviä
* Opettaja - voi tarkastella kursseille ilmoittautuneita opiskelijoita sekä heidän edistymistään ja lisätä kursseja ja materiaaleja ja mahdollisesti lisätä muita     opettajia
* Ylläpitäjä - voi tarkastella ja poistaa muita käyttäjiä ja jakaa tai poistaa käyttöoikeuksia

  Oikeudet päivittyvät vielä...
  
Lisäksi kursseille voi lisätä tekstimateriaalia ja monivalintatehtäviä. Tehtävät voi tarkistaa automaattisesti.

Sovellukseen pääsee [täältä](https://tietokanta-opetussovellus.herokuapp.com/):


## Sovelluksen tila tällä hetkellä:

Sovelluksen tila on vielä turhan vaiheessa, sillä ulkonäkö on kolkko eikä kursseihin liittyvää toiminnallisuutta ole vielä. Taulut kursseille on kuitenkin luotu ja jotain tiedostoja ennalta. 

Sovelluksen etusivulta pääsee luomaan käyttäjän, joka saa automaattisesti opiskelijan oikeudet. Opiskelijana pääsee tarkastelemaan omaa profiiliaan, mutta ei juuri muuta. Linkkejä on valmiiksi tehty, mutta osa ei johda mihinkään.

Ylläpitäjän "ominaisuuksia" pääsee tarkastelemaan seuraavilla tunnuksilla:

käyttäjätunnus: admin001
salasana: testiadmin

Ylläpitäjänä on alustava linkki käyttöoikeuksien jakamiseen, mutta toistaiseksi lomake ei vielä tee mitään.. Käyttöoikeuksien muuttamiseen tulee antaa tunnus ja salasana, tätä kirjoittaessani tajusin, että editprivilege-sivulle päästyään oikeuksien muuttaminen varmaan onnistuu millä tahansa tietokannassa olevilla tunnuksilla eikä vain ylläpitäjän, mikä ei ole tietenkään tarkoitus. Opettajiin liittyvää toiminnallisuutta ei ole vielä, mutta oikeudet voi tarkistaa. 

## Muita tiedossa olevia ongelmia:
Etusivulla on linkki vain käyttäjän omaan profiiliin, mutta manuaalisesti pystyy vaihtamaan URL:sta id:n toiseksi. Kuitenkin pitäisi onnistua vain ylläpitäjän oikeuksilla. 
Sovelluksen ulkonäölle en ole ehtinyt tehdä vielä mitään, esim. linkit samassa kasassa eikä muuta muotoilua.
