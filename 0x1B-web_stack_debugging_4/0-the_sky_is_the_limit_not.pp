# I forgot to put this comment.

exec { 'config':
  command  => "/bin/sed -i \'s/worker_connections .*;/worker_connections 1000000000;/\' /\
etc/nginx/nginx.conf",
}
exec { 'restarting':
  command  => "/usr/sbin/nginx -s reload",
}
