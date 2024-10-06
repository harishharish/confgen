#!/usr/bin/env python

"""Tests for `confgen` package."""

import pytest
from click.testing import CliRunner

from confgen import example_function
from confgen import cli


@pytest.fixture
def response():
    return 1, 2


def test_example_function(response):
    assert example_function(*response) == 3


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "confgen.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help" in help_result.output
    assert "Show this message and exit." in help_result.output
