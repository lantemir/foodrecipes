sudo apt-get update -y
sudo apt upgrade -y

sudo apt -y install openssh-server
sudo systemctl start ssh
sudo systemctl enable ssh

sudo apt -y install net-tools htop git curl nginx
sudo apt -y install gunicorn python3-pip python3-dev python3-venv build-essential libpq-dev unixodbc-dev postgresql postgresql-contrib

# sudo usermod -aG bogdan www-data
sudo usermod -aG ubuntu www-data

ip a

cd ~
mkdir web
cd web
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install wheel
pip install Django gunicorn psycopg2 pyodbc django-cors-headers Pillow
pip install -r requirements.txt

sudo su - postgres
createuser dbdjango
createdb djangodb -O dbdjango

psql djangodb

alter user dbdjango with password '12345678Django$';

\q

exit



sudo nano /etc/systemd/system/gunicorn.socket
<file>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</file>



sudo nano /etc/systemd/system/gunicorn.service
<file>
[Unit]
Description=Gunicorn for the Django example project
Requires=gunicorn.socket
After=network.target

[Service]
Type=notify

User=ubuntu
Group=www-data

RuntimeDirectory=gunicorn
WorkingDirectory=/home/ubuntu/projects/mytodolist
ExecStart=/home/ubuntu/projects/mytodolist/env/bin/gunicorn --workers 3 --bind unix:/run/gunicorn.sock settings.wsgi:application
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
</file>

#settings.wsgi:application проверить settings путь правильный

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable --now gunicorn.service
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# sudo systemctl status gunicorn.service
# sudo systemctl disable gunicorn
# sudo systemctl stop gunicorn





sudo nano /etc/nginx/sites-available/192.168.1.83-http.conf
<file>
server {
listen 80;
listen [::]:80;

server_name localhost 127.0.0.1 192.168.1.83;  

root /home/ubuntu/projects/mytodolist;

location /.well-known/acme-challenge/ {}

location /favicon.ico {
    alias /home/ubuntu/projects/mytodolist/static/logo.png;

    access_log off; log_not_found off;

    expires max;
}

location /robots.txt {
    alias /home/ubuntu/projects/mytodolist/static/robots.txt;

    access_log off; log_not_found off;

    expires max;
}

location /static/ {
    alias /home/ubuntu/projects/mytodolist/static/;

    expires max;
}

location /media/ {
    alias /home/ubuntu/projects/mytodolist/static/media/;

    expires max;
}

location / {
#    include proxy_params;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_buffering off;
    proxy_pass http://unix:/run/gunicorn.sock;
}
}
</file>


sudo ln -s /etc/nginx/sites-available/192.168.1.83-http.conf /etc/nginx/sites-enabled/192.168.1.83-http.conf
sudo service nginx start
# sudo systemctl status nginx.service
# sudo ufw allow 443
# sudo ufw allow 8000
sudo ufw allow 'Nginx Full'
sudo systemctl reload nginx.service
#последний этап
# sudo nginx -t

sudo reboot

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR / 'static')
STATIC_DIR = Path(BASE_DIR / 'static')
STATICFILES_DIRS = [
    Path(BASE_DIR / 'static_external'),
    # Path(BASE_DIR / 'static')
]





python3 manage.py collectstatic

python3 manage.py runserver 0.0.0.0:8000





# https://www.youtube.com/watch?v=iWyblcEi7Bk&list=PLFH0jFGRecS0btzEqlp6f4Ua8FwJYkH1m&index=1
# https://www.youtube.com/watch?v=pV1DuzxPJFw&t=10098s