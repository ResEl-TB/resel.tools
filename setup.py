# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os


version = '0.1-dev'

here = os.path.abspath(os.path.dirname(__file__))

def read_file(*pathes):
    path = os.path.join(here, *pathes)
    if os.path.isfile(path):
        with open(path, 'r') as desc_file:
            return desc_file.read()
    else:
        return ''

desc_files = (('README.rst',), ('docs', 'CHANGES.rst'),
                ('docs', 'CONTRIBUTORS.rst'))

long_description = '\n\n'.join([read_file(*pathes) for pathes in desc_files])

install_requires=['setuptools', 'IPy']


setup(name='resel.tools',
      version=version,
      description="Tools for python Resel scripts",
      long_description=long_description,
      platforms = ["any"],
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
      keywords="tools python",
      author="voileux",
      author_email="voileux@resel.fr",
      url="''",
      license="BSD",
      packages=find_packages("src"),
      package_dir = {"": "src"},
      namespace_packages=["resel"],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      is_valid_ip = resel.tools:is_valid_ip_main
      ip_in_subnet = resel.tools:ip_in_subnet_main
      add_host_2_dhcpd = resel.tools:add_2_dhcpd
      """,
      )

# vim:set et sts=4 ts=4 tw=80:
