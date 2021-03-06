import os
from setuptools import setup
import versioneer


filename = os.path.join(os.path.dirname(__file__), 'requirements.txt')
requirements = open(filename).read().splitlines()

setup(
    name='ordia',
    author='Finn Aarup Nielsen',
    author_email='faan@dtu.dk',
    cmdclass=versioneer.get_cmdclass(),
    description='Ordia - lexical data in Wikidata',
    license='Apache 2.0',
    keywords='wikidata',
    url='https://github.com/fnielsen/ordia',
    packages=['ordia'],
    package_data={},
    install_requires=requirements,
    long_description='',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        ],
    tests_require=['pytest', 'flake8'],
    version=versioneer.get_version(),
)
