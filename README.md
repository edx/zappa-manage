# Zappa Bot Manage

### To Do
- [x] Repo Name
  - `zappa_manage`
- [x] Figure out how to publish to `edX.org` repo
  - Change url in `setup.py`
- [x] Ask Cory about ...
  - `LICENSE` : Do we need one? If so, is the MIT License ok? Otherwise, delete the file and references in `setup.py`
    - Internal product so no license needed
  - `zappa_manage/tests/` : Is it necessary? If so, here's the [guide](https://python-packaging.readthedocs.io/en/latest/testing.html). Otherwise, delete the directory.
    - No need for tests at the moment.
  - `bin/` : Does this have CLI usage? If so, here's the [guide](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html). Otherwise, delete the repository.
    - It does have cli usage since it's used when deploying lambdas envs in GoCD.
