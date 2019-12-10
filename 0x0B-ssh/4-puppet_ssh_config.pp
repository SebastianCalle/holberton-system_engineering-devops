# configurate ssh_config
exec { 'auth':
  path    => '/bin'
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config'
}
