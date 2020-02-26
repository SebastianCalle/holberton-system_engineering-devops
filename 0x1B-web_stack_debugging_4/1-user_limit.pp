# Update limit hard and soft
exec { 'fix-hard-and-soft':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 50' /etc/security/limits.conf;\
  sed -i 's/holberton soft nofile 4/holberton soft nofile 40' /etc/security/limits.conf",
  path    => '/usr/bin:/usr/sbin:/bin'
}
