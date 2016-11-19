from setuptools import setup, find_packages

setup(
    name='iShovel',
    packages=find_packages(),
    version='1.0.0',
    description='Disruptive language picker for teams in a hurry',
    long_description='Digs out the best language for you, disruptively',
    author='Prabhakar Gupta <prabhakargupta267@gmail.com>, Mayank Badola <badola21295@gmail.com>',
    url='https://github.com/prabhakar267/iShovel',
    download_url='https://github.com/prabhakar267/iShovel/tarball/1.0.0',
    keywords=['project', 'language', 'picker', 'team', 'hack', 'hackathons', 'disruptive', 'troll'],
    license='MIT',
    include_package_data = True,
    install_requires=[
        'requests==2.11.1',
        'tabulate==0.7.7',
        'termcolor==1.1.0'
    ],
)
