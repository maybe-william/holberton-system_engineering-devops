package { 'nginx':
  ensure => present,
}

file { [ '/etc', '/etc/nginx', '/etc/nginx/sites-available', '/var', '/var/www', '/var/www/html', '/var/www/err', '/var/www/err/html' ]:
  ensure => 'directory',
}

file { 'index':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => "Holberton School\n",
}

file { '404':
  ensure  => present,
  path    => '/var/www/err/html/404.html',
  content => "Ceci n'est pas une page\n",
}

file { 'nginx-config':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n\terror_page 404 /404.html;\n\tlocation /404.html {\n\t\troot /var/www/err/html;\n\t\tinternal;\n\t}\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n}\n"
}

exec { 'restart nginx':
  command => '/usr/bin/pkill nginx; /usr/sbin/nginx',
}

