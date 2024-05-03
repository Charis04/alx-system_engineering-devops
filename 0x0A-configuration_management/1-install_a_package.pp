# This Puppet manifest installs Flask version 2.1.0 using pip3

class { 'python::pip': }

package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
