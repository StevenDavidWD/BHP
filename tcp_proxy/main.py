import sys
import config
import server

def main():
	if len(sys.argv) < 5:
		print
		print "Usage: python main.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
		print "Example: python main.py 127.0.0.1 9000 10.20.30.40 9000 True"
		print
		sys.exit(0)

	config.local_host = sys.argv[1]
	config.local_port = int(sys.argv[2])

	config.remote_host = sys.argv[3]
	config.remote_port = int(sys.argv[4])

	config.receive_first = sys.argv[5]

	if "True" in config.receive_first:
		config.receive_first = True

	server.server_loop()

if __name__ == '__main__':
	main()