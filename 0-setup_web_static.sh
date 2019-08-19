#!/usr/bin/env bash
#Install Ngnix server, create folders, create symbolic link, give ownership, retart
apt-get -y -update nginx
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'Holbeton School' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubunt /data/

sudo sed -i "/^}/ i\ \location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
service nginx restart