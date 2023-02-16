"""
Haby create command implementation
"""

import click


@click.command()
def new():
    click.echo('New command')
