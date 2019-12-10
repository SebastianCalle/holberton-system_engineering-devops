# configurate ssh_config
excec { 'ssh_config':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config'
}
