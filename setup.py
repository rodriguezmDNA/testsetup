from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='testsetup',
      version='0.0',
      description='test packaging python code',
      url='https://github.com/rodriguezmDNA/testsetup',
      author='Joel Rodriguez Medina',
      author_email='joelrome88+code@gmail.com',
      packages=['src'],
      install_requires=required,
      long_description=open('README.md').read()
      )
