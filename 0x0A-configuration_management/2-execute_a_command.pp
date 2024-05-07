# This Puppet manifest kills processes named killmenow using pkill

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
