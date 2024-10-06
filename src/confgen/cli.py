#!/usr/bin/env python3

"""Console script for confgen."""
import sys

import typer

PACKAGE = "confgen"

app = typer.Typer()


@app.command()
def func():
    """Console script for confgen."""
    print(f"Replace this message by putting your code into {PACKAGE}.cli.main")
    print("See click documentation at https://typer.tiangolo.com/")
    return 0


@app.command()
def test(name: str):
    """Console script for confgen."""
    print(f"{str}")
    return 0

# get the click function. For use with sphinx-click
main = typer.main.get_command(app)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
