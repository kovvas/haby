"""
Haby log command implementation
"""

import click


@click.command()
def log():
    click.echo('Log command')
