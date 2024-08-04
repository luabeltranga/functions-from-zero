#!/usr/bin/env python3
import click
from mylib.bot import scrape


@click.command()
@click.option(
    "--name", help="webpage we want to scrape"
)
@click.option(
    "--lenght", help="number of sentences", default=1
)
def cli(name, lenght):
    result = scrape(name, lenght)
    click.echo(click.style(f"{result}", fg="blue", bg="white"))


if __name__ == "__main__":
    cli()
