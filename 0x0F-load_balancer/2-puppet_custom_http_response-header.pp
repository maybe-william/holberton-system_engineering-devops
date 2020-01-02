# Install nginx on an ubuntu 16.06 server
include stdlib

# install nginx
package { 'nginx':
  name => 'nginx',
}

$header = generate('/bin/cat', '/etc/hostname')

# configure custom header
file_line { 'custom_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => '^server {',
  line   => "add_header X-Served-By ${header};",
}

# start nginx
exec { 'start_server':
  command => '/usr/sbin/service nginx start',
}
exec { 'reload_server':
  command => '/usr/sbin/service nginx reload',
}
exec { 'restart_server':
  command => '/usr/sbin/service nginx restart',
}
