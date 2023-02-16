"""
Haby info command implementation
"""

import click


@click.command()
def info():
    click.echo('Info command')
