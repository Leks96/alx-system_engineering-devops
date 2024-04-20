#executes a bash command
exec { 'kill':
  command  => 'pkill killmenow',
  path     => '['/usr/bin', '/usr/sbin']',
  provider => 'shell',
}