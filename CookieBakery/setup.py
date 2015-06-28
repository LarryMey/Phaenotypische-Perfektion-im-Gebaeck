from setuptools import setup, find_packages
import sys, os

version = '0.1'

tests_require = [
      'pytest',
]

setup(name='CookieBakery',
      version=version,
      description="Phänotypische Perfektion im Gebäck",
      long_description="""\
Phänotypische Perfektion im Gebäck""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Larissa Meyer, Stefan Walluhn',
      author_email='hallo@larissa.io',
      url='www.larissa.io',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      extra_requires = {
          'tests': tests_require,
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
)
