# fix file limit
exec { 'fix-for-nginx':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'sed -i s/15/4096/ /etc/default/nginx'
}
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
