# I forgot to put this comment.

exec { 'phpp':
  command  => "/bin/sed -i \'s/phpp/php/\' /\
var/www/html/wp-settings.php",
}
