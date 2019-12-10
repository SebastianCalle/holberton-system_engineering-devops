# configurate ssh_config
exec { 'ssh_config':
  command  => '/bin/echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" > /etc/ssh/ssh_config'
}
