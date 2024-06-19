from setuptools import setup, find_packages

setup(
    name='wnstcli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'wnstcli=src.cli:cli',
        ],
    },
    url='https://github.com/winstonsec/wnstcli',
    author='Jonatas Winston',
    author_email='your.email@example.com',
    description='A modular CLI tool',
)
