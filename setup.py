"""Minimalny przykład wykorzystanie modułu setuptools"""
from setuptools import setup


setup(
    name="Hello World",  # nazwa projektu
    version=1.0,  # wersja
    description="Przykład użycia setuptools",  # krótki opis
    author="Tomasz Golan",  # autor
    author_email="tomasz.golan@uwr.edu.pl",  # adres mailowy autora
    license="MIT",  # licencja
    url="https://github.com/TomaszGolan/setuptools_helloworld",  # strona projektu
    packages=["hello_world"],  # paczki, które należy uwzględnić przy instalacji
    install_requires=["click"],  # zależności
    entry_points={'console_scripts': "hello=hello_world.hello:main"}  # polecenie=paczka.moduł:funkcja
)                                                                     # czyli którą funkcję wywołać
                                                                      # gdy uruchomimy program danym poleceniem