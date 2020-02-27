# This file sets up the web_static deployment

package { 'nginx':
  name => 'nginx',
}

file { [ '/data', '/data/web_static', '/data/web_static/shared', '/data/web_static/releases', '/data/web_static/releases/test' ]:
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
}

file { '/data/web_static/releases/test/index.html':
  content => '(web_static content placeholder)',
  owner   => ubuntu,
  group   => ubuntu,
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => ubuntu,
  group  => ubuntu,
}

file { [ '/etc', '/etc/nginx', '/etc/nginx/sites-available' ]:
  ensure => directory,
}

file { '/etc/nginx/sites-available/default':
  content => "server {\n\tadd_header X-Served-By ${hostname};\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\terror_page 404 /404.html;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n\tlocation /404.html {\n\t\troot /var/www/err/html;\n\t\tinternal;\n\t}\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n}\n"
}

exec {'reload_nginx':
  command => '/usr/sbin/service nginx restart',
  require => File['/etc/nginx/sites-available/default'],
}
