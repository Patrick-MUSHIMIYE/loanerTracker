import click
from commands.create import create
from commands.add import add


@click.group()
def main():
    """Laptop Loaner Tracking System"""
    pass

main.add_command(create)
main.add_command(add)

if __name__ == '__main__':
    main()
