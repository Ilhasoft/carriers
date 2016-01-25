# -*- coding: utf-8 -*-
from distutils.core import setup

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]
install_requires = [
    'django>=1.8.4',
]

setup(
    name='ilhasoft-carriers',
    version='0.1',
    author='Teeh Amaral - Ilhasoft',
    author_email='ed.amaral@ilhasoft.com.br',
    packages=[''],
    url='https://github.com/Ilhasoft/carriers',
    license='BSD licence, see LICENCE.txt',
    description='Library consultation phone carriers around the world.',
    long_description=open('README.md').read(),
    zip_safe=False,
    download_url="https://github.com/Ilhasoft/carriers/archive/master.zip",
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
