#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo -e "Hello There!\nGeneral Kenobi!" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s.^\tlocation / {.\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {." /etc/nginx/sites-available/default
service nginx restart
