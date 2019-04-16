from sh import git, ssh


branch = git.bake('branch')
myssh = ssh.bake('username@hostname')

