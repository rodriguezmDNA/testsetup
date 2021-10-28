from setuptools import setup, find_packages

### Resources
# https://medium.datadriveninvestor.com/how-to-make-the-package-in-python-a82292aeb775
# https://www.youtube.com/watch?v=GIF3LaRqgXo&t=1s
# how to setup a venv: https://www.youtube.com/watch?v=GaWs-LenLYE

#with open('requirements.txt','r') as f:
#    required = f.read().splitlines()

with open('README.md','r') as fh:
    long_desc = fh.read()

setup(name='helloworld',
      version='0.0.2',
      description='test packaging python code',
      url='https://github.com/rodriguezmDNA/testsetup',
      author='Joel Rodriguez Medina',
      author_email='joelrome88+code@gmail.com',
      package_dir={'': 'src'},
      py_modules = ['helloworld','mymod','hi'],
      #packages=find_packages(),
      #install_requires=required,
      install_requires=['pandas'],
      long_description=long_desc,
      long_description_content_type='text/markdown'
      )
