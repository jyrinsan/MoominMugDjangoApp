# MoominMugDjangoApp

## Yleiskuvaus
MoominMug on Djangolla toteutettu webbisovellus, jossa voi webbiselaimella selata muumimukieni listaa, sekä lisätä, muokata ja poistaa mukeja. Jokaisesta mukista tallennetaan vähintään kuva ja lempinimi sekä muita tietoja kuten virallinen nimi, valmistusvuosi sekä värit, hahmot ja teemat, jotka mukin liittyy. Selaus on mahdollista ilman kirjautumista julkisesti internetissä. Kaikkeen tallentamiseen pitää olla kirjautunut käyttäjä. Vain superuser(=minä) voi luoda uusia käyttäjiä admin-käyttöliittymältä, sillä enhän halua, että kukaa muu kuin luottoperheenjäsen tallentaa tietoja mukeistani.

## Projektin tarve
Sovelluksen tarve nousi siitä, että kerään muumimukeja, ja niitä on hyllyssä yli 60kpl. Kaupassa kun törmään johonkin ihanaan muumimukiin, en usein muista onko minulla se jo, kuinka ihanaa olisikaan katson kännykästä asia. Lisäksi äitini ja jotkut muut sukulaiset usein antavat minulle muumimukeja, mutteivat tietä mitä minulla jo on. Sovelluksella kaikki voisivat tarkistaa asian.

Haaga-Helian Python weppipalvelu - ideasta tuotantoon kurssin loppuprojekti

Sovelluksen tekijä: Sanna Jyrinki

Sovelluksen lisenssi: [GNU GENERAL PUBLIC LICENSE2](../LICENSE)

## Suunnitelma

- moominproject/settings.py
- moominproject/urls.py
- moominmug/models.py
- moominmug/views.py
- moominmug/templates/moominmug/*
- moominmug/registration/login.html

Models
- Mug
- Color
- Theme
- Figure

Views
- ListView
- DetailView
- UpdateView
- CreateView
- DeleteView
- Login ja Logout

Templates 
- base.html
- x_list.html
- x_detail.html
- x_form.html
- x_confirm_delete.html
- login.html

## Asennus

Kloonaa github repositoryni esim. kotihakemistoosi Linuxille
`git@github.com:jyrinsan/MoominMugDjangoApp.git`

Projektin lataus ja virtuaaliympäristön luonti
```bash
cd ## siirry kotihakemistoosi Linuxissasi
git clone git@github.com:jyrinsan/MoominMugDjangoApp.git # vatii, että olet määritellyt github ssh-avaimen
cd MoominMugDjangoApp
virtualenv --system-site-packages -p python3 env
source env/bin/activate
which pip # tarkastetaan, että polku env:n sisällä
```

Djangon asennus
```bash
micro requirements.txt # sisällöksi django==3.2
pip install -r requirements.txt
django-admin --version # tarkistetaan asennus
```

Luo superuser
```bash
/manage.py createsuperuser
```

Käynnistä kehitysserveri 
```
./manage.py runserver
```

## Testaus

Kirjaudu luomallasi superuserilla sovelluksen admin-käyttöliittymään (tarkista ip kehitysserverin käynnistymisestä ja vaihda tarvittaessa 
```
http://127.0.0.1:8000/admin
```

Webbisovellukseen pääset
```
http://127.0.0.1:8000/mugs
```
