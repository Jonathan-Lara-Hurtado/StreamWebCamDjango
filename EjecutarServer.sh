#!/bin/bash
#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput -c
#python3 manage.py collectstatic --noinput
sudo usermod -a -G video $LOGNAME 

#chown www-data:www-data "/home/<volumenPersistente>/db.sqlite3"
ARGS=""
ARGS="$ARGS --log-to-terminal"
ARGS="$ARGS --port 8080"
ARGS="$ARGS --user www-data --group www-data"

ARGS="$ARGS --url-alias /static /home/vigilancia/ArchivosEstaticos/"
ARGS="$ARGS --url-alias /ArchivosMedia /home/vigilancia/ArchivosMedia/"
ARGS="$ARGS --url-alias /favicon.ico /home/vigilancia/ArchivosEstaticos/"
ARGS="$ARGS --limit-request-body 762144000"

exec mod_wsgi-express start-server $ARGS DjangoOpencv/wsgi.py