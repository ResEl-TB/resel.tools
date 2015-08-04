.. contents::

Introduction
============

Tools for python Resel scripts

Installation
============
git clone https://github.com/ResEl-TB/resel.tools.git
cd resel.tools
python setup.py install 



NETWORK
===========

Some Network tools to check IPv4

is_valid_ip
-----------
Check if an IPv4 address is valid 

    is_valid_ip [-h] ip

check if ip is valid

positional arguments:
  ip          an IPv4 address

optional arguments:
  -h, --help  show this help message and exit

ip_in_subnet
-------------
Check if an IPv4 address is in a Subnet 

    ip_in_subnet [-h] ip subnet

check if ip is valid

positional arguments:
  ip          an IPv4 address
  subnet      an IPv4 subnet

optional arguments:
  -h, --help  show this help message and exit


DHCPD
===========

Tools to manipulate an isc-dhcpd server

