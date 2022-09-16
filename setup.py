import setuptools
from rambler_google_activator.version import Version


setuptools.setup(name='rambler_google_activator',
                 version=Version('0.1.0').number,
                 description='Rambler.ru Google Activator',
                 long_description=open('README.md').read().strip(),
                 author='@KM8Oz',
                 author_email='kimo@oldi.dev',
                 url='http://path-to-my-packagename',
                 py_modules=['rambler_google_activator'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=True,
                 keywords='Rambler.ru, Google, Activator, Auth',
                 classifiers=['Rambler.ru', 'Google', 'Activator', 'Auth'])
