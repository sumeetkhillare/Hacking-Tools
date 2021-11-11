
from setuptools import setup, find_packages
from hackingtools.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='hackingtools',
    version=VERSION,
    description='Hack the systems using HackingTools',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Sumeet Khillare',
    author_email='sumeetkhillare10@gmail.com',
    url='https://github.com/cur53onu/Hacking-Tools',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'hackingtools': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        hackingtools = hackingtools.main:main
    """,
)
