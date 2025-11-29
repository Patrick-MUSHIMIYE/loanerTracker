import click
import pandas as pd
import os

@click.command()
@click.option('--file', help='create a file name')
def create(file):
    """ Command to create a file"""
    if os.path.exists(file):
        click.echo(f"Error: File {file} already exists!")
        return

    # Create empty DataFrame with required columns
    df = pd.DataFrame(columns=['ID', 'Username', 'SerialNumber'])
    
    # Save to CSV
    df.to_csv(file, index=False)
