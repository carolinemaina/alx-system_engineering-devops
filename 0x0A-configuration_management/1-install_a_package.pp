#install flask 2.1.0 from pip3

$flask_version = '2.1.0'

exec { 'install_flask':
  command => "${::python3::executable} -m pip install Flask==${flask_version}",
  path    => [$::python3::bin],
  unless  => "${::python3::executable} -m pip show Flask | grep Version | grep -q ${flask_version}",
}
