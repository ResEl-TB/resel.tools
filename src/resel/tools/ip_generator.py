from IPy import IP
import argparse

import sys


def is_valid_subnet(ip):
	"""
	Check if ip is a valid ip.
	>>> is_valid_subnet('192.168.0.1/24')
	True
	
	>>> is_valid_subnet('192.168.0.256')
	192.168.0.256 is not a valid ip
	False
	
	"""
	
	try:
		IP(ip, make_net=True)
		return True
	except:
		print('%s is not a valid ip' %ip)
		return False
		

def is_valid_netmask(netmask):
	"""
    Check if netmask is a valid ipv4 netmask.

	Netmask is a integer
	>>> is_valid_netmask("aa")
	False

	Netmask is less than 32 	
	>>> is_valid_netmask(34)
	False
		
	>>> is_valid_netmask(24)
	True
	
	"""
	
	try:
		netmask = int(netmask)
		if 0 < netmask < 32:
			return True
		else:
			return False
	except:
		return False


def ip_generator(prefix, netmask):
	""" generate a new subprefix with netmask length 
		from prefix 

	>>> my_gen = ip_generator('192.168.1.0/24' , '29')
	>>> my_gen.next()
	IP('192.168.1.0/29')
	>>> my_gen.next()
	IP('192.168.1.8/29')
	
	>>> my_gen2 = ip_generator('192.168.1.0/30','29')
	>>> my_gen2.next()
	netmask is less than prefix length

	
	"""
	
	is_valid_subnet(prefix)
	is_valid_netmask(netmask)

	prefix = IP(prefix, make_net = True)
	netmask = int(netmask)
	try:
		if prefix.prefixlen() > netmask:
			raise Exception('prefixLenError')	
			
		count = 0
		new_subnet = IP(prefix.int() + count * (2 ** (32 - netmask)))
		while prefix.overlaps(new_subnet):
			yield(new_subnet.make_net(netmask))
			count +=1
			new_subnet = IP(prefix.int() + count * (2 ** (32 - netmask ) ))
		
	except Exception as inst:
		if inst.args == ('prefixLenError', ): # because Exception is a tuple
			print('netmask is less than prefix length')
			yield
			

def main(settings):  # pragma: no cover
	
	for subnet in ip_generator(settings['prefix'], settings['netmask']):
		print subnet


if __name__ == '__main__':  # pragma: no cover
    parser = argparse.ArgumentParser(description='IP generator')
    # options
    parser.add_argument('-t', '--test', action="store_true")
    parser.add_argument('-v', '--verbose', action='count', default=0)
    # required args
    parser.add_argument('prefix', help="Please provide a prefix")
    parser.add_argument('netmask', help="Please provide a netmask")
    args = parser.parse_args()
    settings = vars(args)

    if args.test:
        import doctest
        # by default, when all tests are OK, there is no verbose ouput, then we
        # have to force the verbose mode in this case.
        tests = doctest.testmod(verbose=args.verbose >= 1,
                                 optionflags=doctest.ELLIPSIS)
        sys.exit(tests.failed)

    # with sys.exit we ensure to return a standard succes(0) or error (1) code
    sys.exit(not main(settings))

