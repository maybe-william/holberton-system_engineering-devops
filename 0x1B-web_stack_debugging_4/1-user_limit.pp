# I forgot to put this comment.

exec { 'config':
  command  => "/bin/sed -i \'s/holberton/#holberton/\' /\
etc/security/limits.conf",
}
