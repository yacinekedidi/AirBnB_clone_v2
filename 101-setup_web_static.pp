# Add HTTP header Puppet

exec { 'Nginx setup':
command => 'apt-get -y update;
apt-get -y install nginx;
mkdir -p /data/web_static/shared/;
mkdir -p /data/web_static/releases/test/;
echo "Holberton" > /data/web_static/releases/test/index.html;
ln -fs /data/web_static/releases/test/ /data/web_static/current;
chown -R ubuntu:ubuntu /data/;

printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /usr/share/nginx/html;
    index  index.html index.htm;

    location /hbnb_static {
    	alias /data/web_static/current;
    	index  index.html index.htm;
    }

    location /redirect_me {
        return 301 http://youtube.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /usr/share/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default;
sudo service nginx restart;
',
provider   => 'shell',
}
