# configurate ssh_config
excec { 'ssh_config':
  command => echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config
}
