import click
from commands.create import create


@click.group()
def main():
    """Laptop Loaner Management System"""
    pass

main.add_command(create)
if __name__ == '__main__':
    main()
