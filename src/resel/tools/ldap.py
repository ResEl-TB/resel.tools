#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import ldap
import sys
import argparse

def ldap_search(baseDN, searchFilter):
	""" Search in the ResEl LDAP with the given parameters

	>>> ldap_search('ou=machines,dc=resel,dc=enst-bretagne,dc=fr', '(Zone=User)')
	"""
	try:
		try:
			l = ldap.open('ldap.maisel.enst-bretagne.fr')
			l.protocol_version = ldap.VERSION3
		except ldap.LDAPError, e:
			print(e)

		retrieveAttributes = None
		searchScope = ldap.SCOPE_SUBTREE

		try:
			ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
			result_type, result_data = l.result(ldap_result_id, 0)

			if (result_data == []):
				sys.exit(0)
			else:
				if result_type == ldap.RES_SEARCH_ENTRY:
					search_results = result_data[0]
					return search_results

		except ldap.LDAPError, e:
			print(e)

	except NameError:
		print("Undefined parameters")

def ldap_search_main():
	# Liste des arguments du script
    parser = argparse.ArgumentParser(description='Search in the ResEl LDAP with the given parameters')
    parser.add_argument('baseDN', type=str,  help='The dn in which were are searching')
    parser.add_argument('searchFilter', type=str, help='Filter for our search in the specified dn')
    args = parser.parse_args()
    if ldap_search(args.baseDN, args.searchFilter):
        return ldap_search(args.baseDN, args.searchFilter)