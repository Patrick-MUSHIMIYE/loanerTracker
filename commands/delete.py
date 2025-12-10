import click
import os
import pandas as pd

@click.command()
@click.option('--filename', required=True, help='delete collected laptop')
@click.option('--username', required=True, prompt=("enter username"), help='username')
@click.option('--sn', required=True, type=str, prompt=("enter serial"), help='Serial Number')

def delete(filename,username,sn):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            df = pd.read_csv(f)
            if str(username) in df['Username'].values and str(sn) in df['SerialNumber'].values:
                print("match")
            else:
                 print("doesn't match")   
    else:
        print(f'Error: {filename} does not exit')
