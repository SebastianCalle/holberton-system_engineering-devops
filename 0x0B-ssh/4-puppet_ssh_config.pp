# configurate ssh_config
excec { 'auth':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config'
}
