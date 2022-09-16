import setuptools
from rambler_google_activator.version import Version


setuptools.setup(name='rambler_google_activator',
                 version=Version('0.1.0').number,
                 description='Rambler.ru Google Activator',
                 long_description_content_type="text/markdown",
                 long_description=open('README.md').read().strip(),
                 author='@KM8Oz (kmoz000)',
                 author_email='<kimo@oldi.dev>',
                 url='https://github.com/KM8Oz/rambler-google-activator.git',
                 py_modules=['rambler_google_activator'],
                 install_requires=[],
                 license='MIT License',
                 keywords=['Rambler.ru', 'Google', 'Activator', 'Auth'],
                 classifiers=['Development Status :: 3 - Alpha', 'Topic :: Communications :: Email', 'Topic :: Communications :: Email :: Post-Office :: IMAP'])
