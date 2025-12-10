import click
import pandas as pd
import os


@click.command(name='list')
@click.option('--filename', required=True, help='file name')
def list_items(filename):

    """List all laptops in the system"""
    if not os.path.exists(filename):
        click.echo(f"Error: Filename {filename} does not exist!")
        return

    df = pd.read_csv(filename)

    if df.empty:
        click.echo("No laptops found!")
        return


    click.echo("\nlist of All Loaner laptop in the system:")
    click.echo("-" * 80)
    for _, row in df.iterrows():
        click.echo(f"ID: {row['ID']}, Username: {row['Username']}, SN: {row['SerialNumber']}")
    click.echo("-" * 80)