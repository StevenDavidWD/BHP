import sys

def usage():
	print
	print "BHP Net Tool"
	print
	print "Usage: bhpnet.py -t target_host -p port"
	print "-l --listen                -listen on [host]:[port] for incoming connections" 
	print "-e --execute=file_to_run   -execute the given file upon receiving a connection"
	print "-c --command               -initialize a command shell"
	print "-u --upload=destination    -upon receiving connection upload a file and write to [destination]"
	print
	print
	print "Examples: "
	print "python bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print "python bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
	print "python bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
	print "echo 'ABCDEFG' | python bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
	print
	sys.exit(0)