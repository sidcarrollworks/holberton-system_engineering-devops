#replace extension for file
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => '/usr/bin/',
  onlyif  => 'test -e /var/www/html/wp-settings.php'
}
