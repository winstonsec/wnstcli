import click
import os

@click.command()
@click.argument('option')
def install(option):
    """Command to install security agents"""
    if option == 'qualys':
        install_qualys()
    elif option == 'trend':
        install_trend()
    elif option == 'guardicore':
        install_guardicore()
    elif option == 'sentinel':
        install_sentinel()
    elif option == 'all':
        install_all()
    else:
        click.echo("Invalid option. Available options: qualys, trend, guardicore, sentinel, all")

def install_qualys():
    click.echo("Installing Qualys...")
    # Lógica de instalação do Qualys

def install_trend():
    click.echo("Installing Trend...")
    os.system('sh gbsec/modules/install/scripts/install-linux-trend.sh')

def install_guardicore():
    click.echo("Installing Guardicore...")
    # Lógica de instalação do Guardicore

def install_sentinel():
    click.echo("Installing Sentinel...")
    # Lógica de instalação do Sentinel

def install_all():
    click.echo("Installing all agents...")
    install_qualys()
    install_trend()
    install_guardicore()
    install_sentinel()
