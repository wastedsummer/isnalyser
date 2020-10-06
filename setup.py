from setuptools import setup

setup(
	name='isnalyser', # this is the pip name -> what people pip install
	version='0.0.1', # version of our library
	description='Create Isnad graphs automatically.',
	py_modules=["graph", "ranking"], # list of all the small modules -> what people import
	package_dir={'':'isnalyser'}, # directory, where our source code is
	install_requires= ["pandas>=0.24.2", "graphviz>=0.11.1"], # dependancies
	packages=setuptools.find_packages(), 
	url='',
	author='',
	author_email='',
	include_package_data=True,
	)