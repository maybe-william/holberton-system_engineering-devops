# I forgot to put this comment.

exec { 'config':
  command  => "/bin/sed -i \'s/ULIMIT=\".*\"/ULIMIT=\"-n 1500\"/\' /\
etc/nginx/nginx.conf",
}
exec { 'restarting':
  command => '/usr/sbin/service nginx restart',
  onlyif  => '/usr/sbin/service nginx reload',
}
