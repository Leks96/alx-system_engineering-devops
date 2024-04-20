exec { 'pkill':
  command  => 'pkill killmenow',
  path     => '['/usr/bin', '/usr/sbin']',
  provider => 'shell',
}
