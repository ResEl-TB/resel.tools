#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from IPy import IP
import argparse

def is_valid_ip(ip):
    """Check if ip is a valid ip.

    >>> is_valid_ip('192.168.0.1')
    True
    >>> is_valid_ip('192.168.0.256')
    192.168.0.256 is not a valid ip
    False

    """
    try:
        IP(ip) 
    except: 
        print('%s is not a valid ip' %ip)
        return False
    else:
        return True

def is_valid_ip_main():
    # Liste des arguments du script
    parser = argparse.ArgumentParser(description='check if ip is valid')
    parser.add_argument('ip', type=str,  help='an IPv4 address')
    args = parser.parse_args()
    if is_valid_ip(args.ip):
        print("%s is a valid IPv4 Adress" %args.ip)

   

def ip_in_subnet(ip, subnet):
    """ Check if ip in subnet.
    
    >>> ip_in_subnet('172.22.1.21', '172.22.0.0/24')
    172.22.1.21 not in 172.22.0.0/24
    False

    >>> ip_in_subnet('172.22.256.21', '172.22.0.0/24')
    172.22.256.21 is not a valid ip or 172.22.0.0/24 a valid subnet
    False

    >>> ip_in_subnet('172.22.0.21', '172.22.0.3/24')
    172.22.0.21 is not a valid ip or 172.22.0.3/24 a valid subnet
    False

    >>> ip_in_subnet('172.22.0.21', '172.22.0.0/24')
    True

    """
    try:
        ip = IP(ip) 
        subnet = IP(subnet)

    except: 
        print('%s is not a valid ip or %s a valid subnet' %(ip, subnet))
        return False
    else:
        result = ip in subnet
        if not result:
            print('%s not in %s' %(ip, subnet))
        return result 

def ip_in_subnet_main():
    # Liste des arguments du script
    parser = argparse.ArgumentParser(description='check if ip is valid')
    parser.add_argument('ip', type=str,  help='an IPv4 address')
    parser.add_argument('subnet', type=str,  help='an IPv4 subnet')
    args = parser.parse_args()
    if ip_in_subnet(args.ip, args.subnet):
        print("%s is in %s " %(args.ip, args.subnet) )

 
