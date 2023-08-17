from setuptools import setup, find_packages

setup(
    name='pbroker',
    version='0.1',
    description='Python library: mixing for message borkers',
    url='https://github.com/ydiazn/pbroker',
    author='Yenner J. Diaz-Nuñez',
    author_email='yennerdiaz@gmail.com',
    license='LICENSE.txt',
    packages=find_packages(include=['pbroker']),
    install_requires=[
        'pika==1.3.2',
    ],
    test_suite='tests',
    zip_safe=False
)
