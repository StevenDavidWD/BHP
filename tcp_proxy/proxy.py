import socket
import config
import receive
import handler
import dump
import receive

def proxy_handler(client_socket):

	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remote_socket.connect((config.remote_host, config.remote_port))

	if config.receive_first:
		remote_buffer = receive.receive_from(remote_socket)
		dump.hexdump(remote_buffer)

		remote_buffer = handler.response_handler(remote_buffer)

		if len(remote_buffer) > 0:
			print "[<==] Sending %d bytes to localhost." % len(remote_buffer)
			client_socket.send(remote_buffer)

	while True:
		client_buffer = receive.receive_from(client_socket)
		if len(client_buffer) > 0:
			print "[==>] Received %d bytes from client." % len(client_buffer)
			dump.hexdump(client_buffer)

			client_buffer = handler.request_handler(client_buffer)

			print "[==>] Send to remote."
			remote_socket.send(client_buffer)

		remote_buffer = receive.receive_from(remote_socket)
		if len(remote_buffer) > 0:
			print "[<==] Received %d bytes from remote." % len(remote_buffer)
			dump.hexdump(remote_buffer)

			remote_buffer = handler.request_handler(remote_buffer)

			print "[<==] Send to client."
			client_socket.send(remote_buffer)

		if not len(remote_buffer) or not len(client_buffer):
			client_socket.close()
			remote_socket.close()
			print "[*] No more data. Connection closed."
			break

