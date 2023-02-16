"""
Haby stats command implementation
"""

import click


@click.command()
def stats():
    click.echo('Stats command')
