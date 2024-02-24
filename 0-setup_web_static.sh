#!/usr/bin/env bash
# Setups the webserver for deployment of webstatic
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo -e "Hello There!\nGeneral Kenobi!" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s.^\tlocation / {.\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {." /etc/nginx/sites-available/default
service nginx restart
