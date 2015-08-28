def receive_from(connection):
	receive_buffer = ""
	connection.settimeout(2)

	try:
		while True:
			data = connection.recv(4096)
			if not data:
				break
			receive_buffer += data
	except:
		pass

	return receive_buffer