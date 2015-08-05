#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from IPy import IP
import argparse
import re

from ip_generator import ip_generator 

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

 


def get_mac_from_ip(ip, LOCAL_NET):
    """ Récupère l'adresse MAC associee a l'IP fournie
    
    >>> get_mac_from_ip('172.22.201.1', '22') # '22' pour Brest, '23' pour Rennes

    """

    try:
        if re.search('172.'+ LOCAL_NET + '.(20{1,3}|21{1,3}|220|221|222|223|224|225)', ip) is None:
            print("L'adresse fournie ne fait pas partie du subnet ResEl.")
            return None

        mac = subprocess.Popen(["ip neigh show | grep '{}' | awk '{ print $5 }'".format(ip)], stdout=subprocess.PIPE, shell=True).communicate()[0].split('\n')[0].lower()
        matches = re.search('[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}', mac)

        if matches is None:
            print("Aucun resultat avec l'hote {}".format(ip))
            return None

        if len(matches) != 2:
            print("Mauvais nombre de matches ({}) dans pour {}".format(ip))
            return None

        print("La MAC associee a l'IP {} est {}".format(ip, matches[0]))
        return matches[0]

    except NameError:
        print "Aucune adresse IP fournie"
        return None

def get_mac_from_ip_main():
    # Liste des arguments du script
    parser = argparse.ArgumentParser(description='Get the MAC associated to the given IP')
    parser.add_argument('ip', type=str,  help='an IPv4 address')
    parser.add_argument('LOCAL_NET', type=str,  help='22 for Brest, 23 for Rennes')
    args = parser.parse_args()
    if get_mac_from_ip(args.ip, args.LOCAL_NET) is not None:
        print("%s is associated to %s " %(get_mac_from_ip(args.ip, args.LOCAL_NET), args.ip) )



