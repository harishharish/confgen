<!-- markdownlint-disable MD041 -->

[![Repo][repo-badge]][repo-link] [![Docs][docs-badge]][docs-link]
[![PyPI license][license-badge]][license-link]
[![PyPI version][pypi-badge]][pypi-link]
[![Conda (channel only)][conda-badge]][conda-link]
[![Code style: black][black-badge]][black-link]

<!--
  For more badges, see
  https://shields.io/category/other
  https://naereen.github.io/badges/
  [pypi-badge]: https://badge.fury.io/py/confgen
-->

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/psf/black
[pypi-badge]: https://img.shields.io/pypi/v/confgen
[pypi-link]: https://pypi.org/project/confgen
[docs-badge]: https://img.shields.io/badge/docs-sphinx-informational
[docs-link]: https://pages.nist.gov/confgen/
[repo-badge]: https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff
[repo-link]: https://github.com/harishharish/confgen
[conda-badge]: https://img.shields.io/conda/v/harishharish/confgen
[conda-link]: https://anaconda.org/harishharish/confgen
[license-badge]: https://img.shields.io/pypi/l/cmomy?color=informational
[license-link]: https://github.com/harishharish/confgen/blob/main/LICENSE

<!-- other links -->

# `confgen`

Conformere Generation and Refinement Tool

## Overview

ConfGen package use RDKit for conformer generation and xTB for energy based conformer refinement.  

## Features

Some features...

## Status

This package is actively used by the author. Please feel free to create a pull
request for wanted features and suggestions!

## Quick start

- Clone repo from [github](https://github.com/harishharish/confgen).
- change directory to repo root. (cd confgen/)
- Checkout a branch of interest. (git checkout "name of interest")
- Create python virtual env;
  - Grant execution permission to init_conda_venv.sh bash script, command: ```chmod +x init_conda_venv.sh```
  - Run init_conda_venv.sh, command: ```./init_conda_venv.sh```
  - This will create conda based virtual enviroment (.venv/)
  - Activate conda environment, command: ```conda activate "name of virtual environment"```
  - "name of virtual environment" is whole absolute path of virtual environment folder. It can be also be found using ```conda env list``` command.
- Launch jupyter lab, command: ```jupyter lab```
- Open examples/usage/demo.ipynb 


<!-- 
Use one of the following

```bash
pip install confgen
```

or

```bash
conda install -c harishharish confgen
``` -->

## Example usage

```python
import confgen
```

<!-- end-docs -->

## Documentation

See the [documentation][docs-link] for further details.

## License

This is free software. See [LICENSE][license-link].

## Related work

Any other stuff to metion....

## Contact

The author can be reached at <ch.harish.jangrq@gmail.com>.

## Credits

This package was created using
[Cookiecutter](https://github.com/audreyr/cookiecutter) with the
[usnistgov/cookiecutter-nist-python](https://github.com/usnistgov/cookiecutter-nist-python)
template.
