#!/usr/bin/env python3

import sys

import click


@click.command()
@click.argument("name", required=False, default="world")
def main(name: str) -> None:
    click.echo(f"Hello {name}!")
    click.echo(f"sys.version: {sys.version}")
    click.echo(f"sys.version_info: {sys.version_info}")

if __name__ == "__main__":
    main()
