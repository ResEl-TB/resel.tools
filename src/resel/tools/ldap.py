#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import ldap
import ldap.modlist as modlist
import sys
import argparse

import constantes_admin

def search(dn, filtre):
	""" Search in the ResEl LDAP with the given parameters

	>>> search('ou=machines,dc=resel,dc=enst-bretagne,dc=fr', '(Zone=User)')
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
			ldap_result_id = l.search(dn, searchScope, filtre, retrieveAttributes)
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

def add(dn, attrs):
	"""
	attrs : dictionnary with several keys, such as 'objectclass', 'cn', 'userPassword'

	Add the given object to the given dn

	>>> add('ou=machines,dc=resel,dc=enst-bretagne,dc=fr', '(Zone=User)')
	"""
	try:
		try:
			l = ldap.initialize('ldaps://ldap.maisel.enst-bretagne.fr:389')
			l.protocol_version = ldap.VERSION3
			l.simple_bind_s(ldap_admin, ldap_passwd)
			ldif = modlist.addModlist(attrs)
			l.add_s(dn, ldif)
			l.unbind_s()
			print("Ajout reussi de {} dans {}".format(attrs, dn))

		except ldap.LDAPError, e:
			print(e)

	except NameError:
		print("Undefined parameters")

























