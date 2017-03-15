'''
Główny program. Moduł click wykorzystany jest tylko po to,
żeby zademonstrować opcję install_requires.
'''
import click


def main():
    """Drukuje na ekranie Hello World"""
    click.secho("Hello World!", fg='red')


if __name__ == "__main__":
    main()
