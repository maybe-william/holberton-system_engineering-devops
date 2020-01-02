# Install nginx on an ubuntu 16.06 server

# install nginx
package { 'nginx':
  name => 'nginx',
}

# configure custom header
file_line { 'custom_header':
  ensure => present,
  $header = generate('/bin/cat', '/etc/hostname')
  path   => /etc/nginx/sites-available/default
  after  => 'server {',
  line   => "add_header X-Served-By ${header};",
}

# start nginx
exec { 'start_server':
  command => '/usr/sbin/service nginx start',
}
