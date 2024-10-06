"""
Top level API (:mod:`confgen`)
======================================================
"""

from .core import example_function

try:
    from ._version import __version__
except Exception:
    __version__ = "999"

__author__ = """Harish Jangra"""
__email__ = "ch.harish.jangrq@gmail.com"


__all__ = [
    "example_function",
    "__version__",
]
