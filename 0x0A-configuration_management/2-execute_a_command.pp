# This executes a command to kill a program
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
