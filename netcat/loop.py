import config
import threading
import socket
import handler

def server_loop():
	if not len(config.target):
		config.target = "0.0.0.0"

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((config.target, config.port))

	server.listen(5)

	while True:
		client_socket, addr = server.accept()
		client_thread = threading.Thread(target = handler.client_handler, \
			args = (client_socket, ))
		client_thread.start()