# Projektin toteutus

Asensin koneelle seuraavat ohjelmat
- micro
- pwgen
- virtualenv

Loin kotihakemistossani hakemiston uudelle projektille `miniprojekti`
```bash
cd
mkdir miniprojekti
cd miniprojekti
```

Loin env-virtuaaliympäristön
```bash
virtualenv --system-site-packages -p python3 env
source env/bin/activate
which pip # tarkastetaan, että polku env:n sisällä
```

Asensin djangon 
```bash
micro requirements.txt # sisällöksi django==3.2 Pillow
pip install -r requirements.txt
django-admin --version # tarkistetaan asennus
```

Loin django-projektin, ajoin migraatiot, loin superuserin
```bash
django-admin startproject jyrinkicom
cd jyrinki.com
./manage.py makemigrations
./manage.py migrate 
pwgen -s 20 1
/manage.py createsuperuser
```

Käynnistin serverin `./manage.py runserver`

Loin `moominmugs` sovelluksen
```bash
./manage.py startapp moominmugs
micro jyrinkicom/settings.py # lisätään sovellus INSTALLED_APPS kohtaan
```

- Loin kantamallin `models.py`. 
- Rekisteröin tietokannan `admin.py`
- Ajoin migraatiot
- Lisäsin pari mukia admin-käyttöliittymältä
- templates/moominmug hakemisto
- restarttaan kehitysserverin
- listasivu: urls.py, views.py, *.html
- detail, update, create, delete
- 

Login
- urls.py, views.py
- templates/registration hakemisto
- loginsivu

Imaget
https://stackoverflow.com/questions/42752591/how-to-find-django-imagefield-url