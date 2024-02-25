#!/usr/bin/env puppet
# a puppet script that sets up a client SSH configuration file
# to connect to a server without typing a password

file_line { 'Turn off passwd auth':
	ensure  => present,
	line	=> '	PasswordAuthentication no''
	path	=> '/etc/ssh/ssh_config',
}

file_line { 'Declare identity file'
	ensure	=> present'
	line	=> '	IdentityFile ~/.ssh/school',
	path	=> '/etc/ssh/ssh_config',
}
