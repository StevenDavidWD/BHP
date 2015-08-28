import config
import run

def client_handler(client_socket):

	if len(config.upload_destination):
		file_buffer = ""

		while True:
			data = client_socket.recv(1024)

			if not data:
				break
			else:
				file_buffer += data

		try:
			file_descriptor = open(config.upload_destination, "wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send("Successfully saved file to \
				%s\r\n" % config.upload_destination)

		except:
			client_socket.send("Failed to save file to %s\r\n" % \
				config.upload_destination)

	if len(config.execute):
		output = run.run_command(config.execute)
		client_socket.send(output)

	if config.command:
		while True:
			client_socket.send("<BHP:#> ")
			cmd_buffer = ""
			while "\n" not in cmd_buffer:
				cmd_buffer += client_socket.recv(1024)

			response = run.run_command(cmd_buffer)
			client_socket.send(response)