from setuptools import setup, find_packages

setup(
    name='gbsec',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'gbsec=gbsec.cli:cli',
        ],
    },
    url='https://github.com/grupoboticario/si-cloudsec-gbsec-cli',
    author='Jonatas Winston',
    author_email='jonatas.winston@grupoboticario.com.br',
    description='A modular CLI tool',
)
