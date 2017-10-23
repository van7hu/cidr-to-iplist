from netaddr import IPNetwork
import sys


cidr = sys.argv[1]

def cidrtoips(cidr):
	ips = IPNetwork(cidr)
	with open("tmp.txt", "w+") as f:
		for ip in ips:
			f.write(str(ip) + "\n")

cidrtoips(cidr)
