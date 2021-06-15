import socket 		# socket allows to establish connection over the internet
from IPy import IP	# for conversion of domain name to ip

def scan(target):
	converted_ip = check_ip(target)
	print("\n" + "[-_0 Scanning Target] " + str(target))
	for port in range(1, 82):
		scan_port(converted_ip, port)

def check_ip(ip):
	try:
		IP(ip)
		return(ip) 	# if user inputs ip address simply returns the ip address
	except ValueError:
		return socket.gethostbyname(ip)		# if user inputs domain url then returns the ip address

def get_banner(s): 	#look what service is running in the open ports
	return s.recv(1024)  	# receives 1024 bytes from the output

def scan_port(ipaddress, port):
	try:
		sock = socket.socket() 		# socket descriptor
		sock.settimeout(0.5) 	  # lower the timeout smaller the accuracy but makes the port scanner faster
		sock.connect((ipaddress, port)) 	# will try to connect to the ipaddress and port
		try: 
			banner = get_banner(sock) 		#look what service is running in the open ports
			print("[+] Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
		except:
			print("[+] Open Port " + str(port))
	except:
		pass 	#pass if the port is closed

targets = input("[+] Enter Target/s To Scan(split multiple targets with ,): ")

if ',' in targets:
	for ip_add in targets.split(','):
		scan(ip_add.strip(' '))
else:
	scan(targets)
