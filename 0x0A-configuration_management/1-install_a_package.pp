#Installing a package using puppet

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/bin',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep 2.1.0',
}
