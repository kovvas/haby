"""
Haby delete command implementation
"""

import click


@click.command()
def delete():
    click.echo('Delete command')
