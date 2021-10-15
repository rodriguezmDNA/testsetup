from setuptools import setup, find_packages

with open('requirements.txt','r`') as f:
    required = f.read().splitlines()

with open('README.md','r') as fh:
    long_desc = fh.read()

setup(name='helloworld',
      version='0.0.2',
      description='test packaging python code',
      url='https://github.com/rodriguezmDNA/testsetup',
      author='Joel Rodriguez Medina',
      author_email='joelrome88+code@gmail.com',
      package_dir={'': 'src'},
      py_modules = ['helloworld'],
      #packages=find_packages(),
      install_requires=required,
      long_description=long_desc,
      long_description_content_type='text/markdown'
      )
