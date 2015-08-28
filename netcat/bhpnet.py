import config
import socket
import getopt
import usage
import sender
import loop
import sys

def main():
	if not len(sys.argv[1: ]):
		usage.usage()
	try:
		opts, args = getopt.getopt(sys.argv[1: ], "hle:t:p:cu", ['help', 'listen', 'execute=', 'target=', 'port=', 'command', 'upload'])
	except getopt.GetoptError as err:
		print str(err)
		usage.usage()

	for o, a in opts:
		if o in ('-h', '--help'):
			usage.usage()
		elif o in ('-l', '--listen'):
			config.listen = True
		elif o in ('-e', '--execute'):
			config.execute = True
		elif o in ('-c', '--commandshell'):
			config.command = True
		elif o in ('-u', '--upload'):
			config.upload_destination = a
		elif o in ('-t', '--target'):
			config.target = a
		elif o in ('-p', '--port'):
			config.port = int(a)
		else:
			assert False, "Unhandled Option"

	if not config.listen and len(config.target) and config.port > 0:
		buffer = sys.stdin.read()
		sender.client_sender(buffer)

	if config.listen:
		loop.server_loop()
if __name__ == '__main__':
	main()