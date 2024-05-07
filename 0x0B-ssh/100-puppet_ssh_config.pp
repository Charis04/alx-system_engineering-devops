# This Puppet manifest configures SSH client to use private key for passwordless login

file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  # Add options for private key and disable password authentication
  content => "
  IdentitiesOnly yes
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
  ",
}
