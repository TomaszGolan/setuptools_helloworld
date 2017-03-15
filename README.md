# Hello World

*Hello World* jako przykład użycia modułu *setuptools*. Więcej informacji można znaleźć w dokumentacji.

## Struktura

```
├── hello_world      # paczka hello_world      
│   ├── hello.py     # moduł hello
│   └── __init__.py  # inicjalizacja paczki
├── LICENSE          # plik z licencją
├── README.md        # opis projektu
└── setup.py         # definicja instlacji
```

### setup.py

W pliku `setup.py` wywołujemy funkcję `setuptools.setup` podając informacje o naszym projekcie:

```
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
```

Kluczowe są opcje:

* `packages` - lista paczek, które chcemy włączyć do projektu (w tym przypadku istnieje tylko paczka `hello_world`, ale projekt może być bardziej rozbudowany)
* `install_requires` - lista paczek do zainstalowania (których wymaga nasz projekt do poprawnego działania)
* `entry_points` - tu ustalamy polecenie, którym będziemy uruchamiać nasz program oraz funkcję, która ma być wywołana

W tym przypadku program składa się z jednej paczki `hello_world`, używa modułu `click` a komendą `hello` chcemy wywołać funkcję `main` z modułu `hello` z paczki `hello_world`.

### hello_world

Paczka `hello_world` zawiera tylko plik `__init__.py`, który jest wymagany oraz `hello.py`, w który mieści się nasz cały mini projekt. W `hello.py` definiujemy funkcję `main`, którą chcemy wywołać poleceniem `hello` (po instalacji programu).

Ostatni fragment:

```
if __name__ == "__main__":
    main()
```

nie jest konieczny, ale umożliwia nam uruchomienie `hello.py` bez instalacji, tzn. `python hello.py` (więcej informacji w [notatkach z wykładu](https://github.com/TomaszGolan/js-python)).

## Instalacja

Aby zainstalować program można skorzystać z `pip` lub ręcznie wywołać `setup.py`.

### Metoda pierwsza

```
pip install git+https://github.com/TomaszGolan/setuptools_helloworld.git
```

### Metoda druga

```
git clone https://github.com/TomaszGolan/setuptools_helloworld.git
cd setuptools_helloworld/
python setup.py install
```

## Uruchamianie

Aby uruchomić tak zainstalowany program wystarczy użyć komendy zdefiniowanej z `entry_points`, czyli w tym przypadku `hello`:

```
$ hello
Hello World!
```

Informacje o programie można sprawdzić korzystając z `pip show [nazwa zdefiniowane przez name]`:

```
$ pip show Hello-World
Name: Hello-World
Version: 1.0
Summary: Przykład użycia setuptools
Home-page: https://github.com/TomaszGolan/setuptools_helloworld
Author: Tomasz Golan
Author-email: tomasz.golan@uwr.edu.pl
License: MIT
Location: /home/goran/soft/anaconda3/lib/python3.6/site-packages
Requires: click
```

## Odinstalowanie

Program można odinstalować korzystając z `pip uninstall [nazwa]`:

```
$ pip uninstall Hello-World
```
