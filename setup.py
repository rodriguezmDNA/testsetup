from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='testsetup',
      version='0.0',
      description='test packaging python code',
      url='https://github.com/rodriguezmDNA/testsetup',
      author='Joel Rodriguez Medina',
      author_email='joelrome88+code@gmail.com',
      package_dir={'': 'src'},
      packages=find_packages(),
      install_requires=required,
      long_description=open('README.md').read()
      )
