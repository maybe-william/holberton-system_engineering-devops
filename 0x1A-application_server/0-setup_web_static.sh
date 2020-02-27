#!/usr/bin/env bash
# set up web_static deployment

# install nginx if not installed
sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start

# create all directories and basic files if nonexistant
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
echo "(web_static deployment placeholder)" | sudo tee /data/web_static/releases/test/index.html

# recreate current symlink
sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# change ownership
sudo chown -R ubuntu:ubuntu /data

# set the nginx config file with an alias
echo $'server {\n\tadd_header X-Served-By '"$HOSTNAME"$';\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\terror_page 404 /404.html;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n\tlocation /404.html {\n\t\troot /var/www/err/html;\n\t\tinternal;\n\t}\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n\tlocation / {\n\t\ttry_files $uri $uri/ =404;\n\t}\n}\n' | sudo tee /etc/nginx/sites-available/default

# reload and restart nginx
sudo service nginx reload
sudo service nginx restart
