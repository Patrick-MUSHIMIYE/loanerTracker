import click
import pandas as pd
import os

@click.command()
@click.option('--filename', help='create a file name')
def create(filename):
    """ Command to create a file"""
    if os.path.exists(filename):
        click.echo(f"Error: Filename {filename} already exists!")
        return

    # Create empty DataFrame with required columns
    df = pd.DataFrame(columns=['ID', 'Username', 'SerialNumber'])

    # Save to CSV
    df.to_csv(filename, index=False)
    click.echo(f"{filename} is created")
