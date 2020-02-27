# Debug nginx
exec { 'fix-nginx':
  command => "sed -i 's/-n 15/-n 4096' /etc/default/nginx\
  service nginx stop; service nginx start",
  path    => '/usr/bin:/usr/sbin:/bin'
}
