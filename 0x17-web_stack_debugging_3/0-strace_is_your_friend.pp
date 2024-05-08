# Creates a manifest that fixes phpp extension

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', 'usr/local/bin/'],
}
