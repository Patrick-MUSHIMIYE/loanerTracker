import click
import pandas as pd
import os

@click.command()
@click.option('--filename', help='file name')
@click.option('--id', required=True, type=int, help='Laptop ID')
@click.option('--username', required=True, help='username')
@click.option('--sn', required=True, type=str, help='Serial Number')
def add(filename, id, username, sn):
    """Add a new laptop to the system"""
    if not os.path.exists(filename):
        click.echo(f"Error: Filename {filename} does not exist!")
        return

    df = pd.read_csv(filename)
    
    # Check if ID or SN already exists
    if int(id) in df['ID'].values or sn in df['SerialNumber'].values:
        click.echo("Error: ID or Serial Number already exists!")
        return

    new_row = {'ID': id, 'Username': username, 'SerialNumber': sn}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(filename, index=False)
    click.echo(f"laptop {id} added to the system")
