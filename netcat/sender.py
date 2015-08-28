import socket
import config

def client_sender(buf):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((config.target, config.port))
		if len(buf):
			client.send(buf)

		while True:
			recv_len = 1
			response = ""

			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response += data
				if recv_len < 4096:
					break

			print response

			buf = raw_input("")
			buf += "\n"

			client.send(buf)

	except:
		print "[*] Exception! Exiting."
		client.close()