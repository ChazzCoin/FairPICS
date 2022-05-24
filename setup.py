from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairPICS',
    version='1.3.1',
    description='Source Provider & Topic/Category Analyzer.',
    url='https://github.com/chazzcoin/Fopics',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    package_data={
        'fopResources': ['*.txt', '*.csv']
    },
    install_requires=['FCoRE~=1.0.3'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)