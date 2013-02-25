#!/usr/local/bin/python
from urllib import urlopen
import sys
from os import isatty

def cuturl(input):
	try:
		response = urlopen('http://pycutter.uphero.com/add.php?url=' + input+'&shorten=click+here')
	except Exception, e:
		error('Could not connect to http://pycutter.uphero.com \nException: %s' % e)
	return response.read()

def error(err, value=1):
	print >> sys.stderr, 'Error: ' + err  
	sys.exit(value) 

def help():
	text="""Usage: surl [URLs]
Examples:
$ pycutter
    Display this dialog
$ pycutter http://3novices.blogspot.com
    Retrieve a shortened URL for 'http://3novices.blogspot.com'

Hint:
- URLs which include the ampersand character ('&') must be passed in quotes on the command-line.  Otherwise bash (or whatever shell you use) will be very unhappy."""
	print text
	sys.exit()

# Assumes http:// and rejects other protocols
def is_http(url):
	if '://' in url:
		protocol = url.split('://',1)[0]
		if protocol != 'http':
			error('Protocol %s is not supported' % protocol)
	else:
		url = 'http://'+url
	return url

if __name__ == '__main__':
	args = sys.argv
	#  No arguments?
	if len(args) == 1:
		help()
	# Read URLs from command-line
	else:
		for url in args[1:]:
			print cuturl(is_http(url))
