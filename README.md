# dggs-swg-test

[View Draft Site](https://data-navigator.github.io/dggs-swg-test/)

## Contributing

### Building the Site

The easiest way to install Python with the required packages to build the static site is to use the
Miniconda3 package manager.
It can be downloaded [here](https://conda.io/miniconda.html).

Ensure conda is on the system's PATH and restart the shell.

You can then use the shell command `conda env create -f environement.yaml` to
create the environment.

#### Requirements

- Python 3
  - markdown
  - pyyaml
  - tabulate

### Submitting a DGGS

Create a pull request with the rebuilt site, including the .yaml file
produced when running the OGC SITE test suite against your implementation
in the _data folder.
