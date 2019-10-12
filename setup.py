
from setuptools import setup

setup(name='datapeek',
      version='0.1',
      description='A simple library for dealing with raw data',
      url='https://github.com/sanket1203/spark',
      author='Sanket Patel',
      author_email='sanket.patel@wissen.com',
      license='MIT',
      packages=['datapeek'],
      install_requires=[
                'fuzzywuzzy',
                'pandas'
      ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
