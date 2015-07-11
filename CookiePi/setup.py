from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='CookiePi',
      version=version,
      description="CookieBakery, Raspy parts",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Stefan Walluhn, Larissa Meyer',
      author_email='hallo@larissa.io',
      url='www.larissa.io',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
