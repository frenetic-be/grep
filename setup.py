#!/usr/bin/env python
import grep

from distutils.core import setup

setup(name='grep',
      version=grep.__version__,
      description='Python equivalent to grep',
      long_description='''
      Python equivalent to grep.''',
      author='Julien Spronck',
      author_email='frenticb@hotmail.com',
      url='http://frenticb.com/',
      packages=['grep'],
      license='Free for non-commercial use',
     )