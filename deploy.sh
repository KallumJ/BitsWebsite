ssh hogwarts.bits.team << EOF
	cd /var/flask/bits.team
	screen -X -S Website quit
	logout
EOF

rsync -av --exclude={'.git', '.idea', '.vscode', '__pycache__', '.gitignore', 'README.md', 'deploy.sh', 'players.json', 'whitelist.json'} * hogwarts.bits.team:/var/flask/bits.team

ssh hogwarts.bits.team << EOF
  cd /var/flask/bits.team
  screen -S Website -d -m python3 waitress_server.py -h
EOF
