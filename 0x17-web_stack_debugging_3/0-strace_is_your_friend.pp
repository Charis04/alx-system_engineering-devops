# write puppet manifest to fix server error
exec { 'fix-wordpress-server':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
