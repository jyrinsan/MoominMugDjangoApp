all:
	rsync -v -a -h jyrinkicom moominmugs --exclude=jyrinkicom/settings.py sanna@jyrinki.com:/home/sanna/publicwsgi/jyrinkicom; ssh sanna@jyrinki.com 'source publicwsgi/env/bin/activate; ./publicwsgi/jyrinkicom/manage.py migrate; touch publicwsgi/jyrinkicom/jyrinkicom/wsgi.py'
