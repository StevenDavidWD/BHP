import subprocess

def run_command(command):
	command = command.rstrip()
	try:
		optput = subprocess.check_output(command, \
			stderr = subprocess.STDOUT, shell = True)
	
	except:
		output = "Failed to execute command.\r\n"

	return optput