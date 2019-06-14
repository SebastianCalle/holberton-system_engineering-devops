# Shell Permissions


Learn about the permissions of the files and directories and how to use several commands of the sell

- su betty	- Change the user to betty.
- whoami	- Show the user.
- groups	- Show the groups.
- chwon betty hello - Change the file hello to user betty.
- touch hello - Create empity file call hello.
- chmod u+x hello - Give permission of execution to the file to user.
- chmod u+x,g+x,o+r hello - Give permission of execution to user and group and read others.
- chmod ugo+x hello - Give permission of execution to all .
- chmod 007 hello - The file hello only have permission for the others.
- chmod --reference=olleh hello - The file hello have the same permissions that olleh.
- chmod -R ugo+X . - Give permission recursive.
- mkdir -m 751 dir_holberton - Create a directory whit permissions.
- chgrp holberton hello - Change file hello to group holberton.
- chown -R betty:holberton . Change all files and directorys of betty to holberton
- chown -h betty:holberton _hello - Change the symbolic links of betty to holberton
- chown --from=guillaume betty hello - Change file to betty if the user is guilluame
- telnet towel.blinkenlights.nl - Play start wars IV
