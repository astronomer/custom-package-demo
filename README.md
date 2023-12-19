# Custom package demo

> [!IMPORTANT]  
> This repository serves as a demo for how to structure a custom package.\
> Feel free to copy and adjust to your own needs.

This Python library hosts custom Airflow Operators, Sensors, Notifiers, etc. that are common across **[insert company name]** data teams. This guide will walk you through how this library works, how to use it in your project, making changes, running tests, and contributing your changes.

## Table of Contents

- [Installing the library](#installing-the-library)
- [Using the library](#using-the-library)
- [Versioning](#versioning)
- [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)
- [Contributing](#contributing)
   * [Getting started](#getting-started)
   * [Making changes](#making-changes)
   * [Testing](#testing)
   * [Pull requests](#pull-requests)
   * [Update your project dependency](#update-your-project-dependency)
- [Library structure](#library-structure)
- [How do I ...?](#how-do-i-)

<sub>Table of contents generated using https://derlin.github.io/bitdowntoc.</sub>

## Installing the library

Since this repository is built only for example purposes, we publish a Python package only to [TestPyPI](https://test.pypi.org/project/democorp-airflow). Therefore, you'll need to add TestPyPI as an (extra) index URL. You can install the package using pip:

```bash
pip install -i https://test.pypi.org/simple/ democorp-airflow
```

Or define the package in a requirements.txt file and install using `pip install -r requirements.txt`:

```
--extra-index-url https://test.pypi.org/simple
democorp_airflow
```

## Using the library

Import example:
```python
from democorp_airflow.operators.example import ExampleOperator
```

## Versioning

We use `setuptools-scm` to automatically manage versioning based on git tags. When you create a new tag, the library version is updated accordingly, and a release for the given tag is made. See the files in `.github/workflows` for inspiration.

See [1](https://github.com/pypa/setuptools_scm/), [2](https://www.moritzkoerber.com/posts/versioning-with-setuptools_scm/) for more details.

## Continuous Integration/Continuous Deployment (CI/CD)

Our CI/CD pipeline is managed using GitHub Actions:

- On every commit, syntax checks and unit tests are run to ensure code quality. See `.github/workflows/ci.yaml`.
- When a new tag is pushed, the library is built, published to TestPyPI, and a GitHub release is created. See `.github/workflows/publish.yaml`.

## Contributing

We welcome contributions from every team to improve this library! Here's how you can get started:

### Getting started

1. Clone the repository to your local machine.
1. Create a new branch for your changes: `git checkout -b my-new-feature`.

### Making changes

1. Make your desired changes to the library, following the structure and coding guidelines.
1. Write unit tests for your changes in the `tests/` directory.

### Testing

Before submitting your changes, ensure that all tests pass:

```bash
pytest tests/
```

### Pull requests

1. Commit your changes and push them to your branch.
1. Create a pull request from your branch to the `main` branch.
1. The CI/CD pipeline will automatically run tests on your pull request.
1. Once the tests pass and your code is reviewed, your contribution will be merged into the main repository.

### Update your project dependency

Once a new version of the `custom-package-demo` library is released, you need to update your Airflow project to use it.

1. Update the version constraint in your `requirements.txt` file.   
1. After updating the package, it's crucial to test your project to ensure that the new version works as expected and doesn't introduce any compatibility issues or bugs. Run `astro dev start` to test changes locally.
1. Commit your changes to the requirements.txt file to Git so that other developers can easily reproduce your project environment.

## Library structure

The library is organized as follows:

```
custom_package_demo/
├── hooks/
│   ├── __init__.py
│   └── ...
├── notifiers/
│   ├── __init__.py
│   └── ...
├── operators/
│   ├── __init__.py
│   └── ...
├── sensors/
│   ├── __init__.py
│   └── ...
├── tests/
│   ├── hooks/
│   │   ├── __init__.py
│   │   └── ...
│   ├── notifiers/
│   │   ├── __init__.py
│   │   └── ...
│   ├── operators/
│   │   ├── __init__.py
│   │   └── ...
│   ├── sensors/
│   │   ├── __init__.py
│   │   └── ...
├── README.md
├── pyproject.toml
└── setup.py
```

- `tests/` directory contains unit tests for each component
- `pyproject.toml` is used for package configuration and versioning
- `setup.py` is used for backwards compatibility of newer `pyproject.toml` syntax

Happy coding!

## How do I ...?

Explain usage of custom components here...
