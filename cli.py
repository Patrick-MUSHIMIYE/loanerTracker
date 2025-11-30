import click
from commands.create import create
from commands.add import add
from commands.list import list_items

@click.group()
def main():
    """Laptop Loaner Tracking System"""
    pass

main.add_command(create)
main.add_command(add)
main.add_command(list_items)

if __name__ == '__main__':
    main()


