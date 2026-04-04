# Python: SmartThings

[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](./LICENSE)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]
[![Code Smells][code-smells]][sonarcloud]

Asynchronous Python client for SmartThings.

## About

This package allows you to fetch data from SmartThings.

## Installation

```bash
pip install pysmartthings
```

## Changelog & Releases

This repository keeps a change log using [GitHub's releases][releases]
functionality. The format of the log is based on
[Keep a Changelog][keepchangelog].

Releases are based on [Semantic Versioning][semver], and use the format
of `MAJOR.MINOR.PATCH`. In a nutshell, the version will be incremented
based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](.github/CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Community

For community support and discussions, join the [SmartThings Integrations community on Discord](https://discord.gg/EJYdwMCz7K).

## Setting up development environment

This Python project is fully managed using the [Poetry][poetry] dependency manager. But also relies on the use of NodeJS for certain checks during development.

You need at least:

- Python 3.12+
- [Poetry][poetry-install]
- NodeJS 12+ (including NPM)

To install all packages, including all development requirements:

```bash
npm install
poetry install
```

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

## Authors & contributors

For a full list of all authors and contributors,
check [the contributor's page][contributors].

## License

Licensed under the Apache License, Version 2.0, as found in the [LICENSE](./LICENSE) file.

[build-shield]: https://github.com/pySmartThings/pysmartthings/actions/workflows/tests.yaml/badge.svg
[build]: https://github.com/pySmartThings/pysmartthings/actions
[code-smells]: https://sonarcloud.io/api/project_badges/measure?project=pySmartThings_pysmartthings&metric=code_smells
[codecov-shield]: https://codecov.io/gh/pySmartThings/pysmartthings/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/pySmartThings/pysmartthings
[commits-shield]: https://img.shields.io/github/commit-activity/y/pySmartThings/pysmartthings.svg
[commits]: https://github.com/pySmartThings/pysmartthings/commits/master
[contributors]: https://github.com/pySmartThings/pysmartthings/graphs/contributors
[keepchangelog]: http://keepachangelog.com/en/1.0.0/
[license-shield]: https://img.shields.io/github/license/pySmartThings/pysmartthings.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com/
[project-stage-shield]: https://img.shields.io/badge/project%20stage-stable-green.svg
[python-versions-shield]: https://img.shields.io/pypi/pyversions/pysmartthings
[releases-shield]: https://img.shields.io/github/release/pySmartThings/pysmartthings.svg
[releases]: https://github.com/pySmartThings/pysmartthings/releases
[semver]: http://semver.org/spec/v2.0.0.html
[sonarcloud]: https://sonarcloud.io/summary/new_code?id=pySmartThings_pysmartthings
[pypi]: https://pypi.org/project/pysmartthings/
