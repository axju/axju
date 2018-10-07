from axju.contrib.cli import obj2cli

from axju.me import system, templates, alias


def templates_cli():
    obj2cli(templates)

def system_cli():
    obj2cli(system)

def alias_cli():
    obj2cli(alias, default='run')
