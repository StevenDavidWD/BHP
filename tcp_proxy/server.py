import socket
import config
import threading
import proxy
import sys

def server_loop():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		server.bind((config.local_host, config.local_port))
	except:
		print "[!!] Failed to listen on %s:%d" % (config.local_host, config.local_port)
		print "[!!] Cheak for other listening sockets or correct permissions."
		sys.exit(0)

	print "[*] Listening on %s:%d" % (config.local_host, config.local_port)

	server.listen(5)

	while True:
		client_socket, addr = server.accept()
		print "[==>] Received incomming connectiong from %s:%d" % (addr[0], addr[1])
		proxy_thread = threading.Thread(target = proxy.proxy_handler, args = (client_socket, ))
		
		proxy_thread.start()



