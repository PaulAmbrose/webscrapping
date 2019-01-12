#! /usr/bin/python3

#mapit.py - Launches a map in the browser using an address from the command line or clipboard
#run from command line address is address with spaces only

e.g. 

./mapit.sh 45 Gladstone Street Norwich NR2 3BH

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	#get address from command line
	address = ' '.join(sys.argv[1:])
else:
	#get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)