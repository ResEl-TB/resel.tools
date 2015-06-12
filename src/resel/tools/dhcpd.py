#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse
import shutil
from IPy import IP
from network import is_valid_ip, ip_in_subnet
from  utils import read_file
from ConfigParser import SafeConfigParser
import sys

def parser():
    # Liste des arguments du script
    config = 'config.ini' 
    parser = argparse.ArgumentParser(description='Ajoute une machine au fichier de conf du dhcp')
    parser.add_argument('-c', '--config', default='%s' % config,
                          help='config filename, default is %s' % config)


    parser.add_argument('host', type=str,  help='champ host de la fiche ldap de la machine')
    parser.add_argument('ip', type=str,  help='IPv4 de la machine')
    parser.add_argument('mac', type=str, help='adresse mac de la machine')
    parser.add_argument('hostname', type=str,  help='champ hostname de la fiche ldap de la machine')
    return parser.parse_args()

def get_config(filename):
    parser = SafeConfigParser()
    parser.read(filename)
    return parser._sections

       

def parse_dhcpd_config(filename):
    """ Parse a isc-dhcpd config file.
    return a dict with each static host.
    host alalevee-1 {
      fixed-address 172.22.219.81;
      hardware ethernet  48:5b:39:64:bf:6b;
      option host-name "alalevee";
    }
    lease = { 'alalevee-1' : 
        { 'line' : <line in dhcpd.conf>
        'ip' : 172.22.219.81, 
        'mac' : 48:5b:39:64:bf:6b,
        'hostname' : alalevee }
        ...
        }
    >>> parse_dhcpd_config('tests/dhcpd.conf')
    {'alalevee-1': {'ip': '172.22.219.81', 'line': 9, 'hostname': 'alalevee', 'mac': '48:5b:39:64:bf:6b'}}

    """

    leases = {}
    lines = read_file(filename)
    new_block = False
    for idx, line in enumerate(lines[0:-2]):
        
        if line.startswith('host '):
            new_block = True
            host = line.split()[1]
            leases[host] = {'line': idx +1}
        if line.strip().startswith('fixed-address'):
            leases[host]['ip'] = line.strip().split()[1][0:-1]
        if line.strip().startswith('hardware ethernet'):
            leases[host]['mac'] = line.strip().split()[2][0:-1]
        if line.strip().startswith('option host-name'):
            leases[host]['hostname'] = line.strip().split()[2][1:-2]
        if line.strip().startswith('}'):
            new_block= False

    return leases


def get_hosts(leases):
    """ get list of host in leases
    leases is a dict from parse_dhcpd_config
    return hosts as list
    """
    return leases.keys()

def get_ips(leases):
    """ get list of ips in leases
    leases is a dict from parse_dhcpd_config
    return ips as list for each host in leases dict
    """
    return [leases[host]['ip'] for host in leases]

def get_macs(leases):
    """ get list of macs in leases
    leases is a dict from parse_dhcpd_config
    return macs as list for each host in leases dict
    """
    return [leases[host]['mac'] for host in leases]

def get_hostnames(leases):
    """ get hostnames of ips in leases
    leases is a dict from parse_dhcpd_config
    return hostnames as list for each host in leases dict
    """
    return [leases[host]['hostname'] for host in leases]

def add_2_dhcpd():
    args = parser()
    config = get_config(args.config)
    
    if not is_valid_ip(args.ip):
        sys.exit()
   
    if not ip_in_subnet(args.ip, config['network']['subnet_user1']) and not ip_in_subnet(args.ip, config['network']['subnet_user2']):
        sys.exit()


    

    bad = None
    leases = parse_dhcpd_config(config['dhcpd']['file'] )
    ips = get_ips(leases)
    macs = get_macs(leases)
    hostnames = get_hostnames(leases)

    if args.ip in ips:
        print( [leases[host]  for host in leases if leases[host]['ip'] == args.ip][0])
        bad = True
    if args.mac in macs:
        bad = True
        print( [leases[host]  for host in leases if leases[host]['mac'] == args.mac][0])
    if args.hostname in hostnames:
        bad = True
        print( [leases[host]  for host in leases if leases[host]['hostname'] == args.hostname][0])

    sys.exit(bad)

if __name__ == '__main__':
    main()
