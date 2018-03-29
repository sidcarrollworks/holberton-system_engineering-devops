exec { 'killmenow':
  #kills a process
  command => 'pkill -f killmenow',
  path    => '/usr/bin/'
  provider=> 'shell'
}
