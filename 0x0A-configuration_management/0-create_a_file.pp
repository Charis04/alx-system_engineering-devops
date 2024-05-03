# This Puppet manifest creates a file named school with specific
# ownership, permissions, and content in the /tmp directory

file { '/tmp/school':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0744',
  content => 'I love Puppet',
}
