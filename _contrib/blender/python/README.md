# Introduction

This repo provides tool/tools for:

* Extracting data out of Phabricator in json format (> orig )
* Permit incremental updates of extracted data (not full pulls)
* Caching lookups for several data-types (users present, files to come)
* Converting data from Phabricator to Gitea .yaml files (> convert)
* Prepare converted files to be in proper format for Gitea import


# Requirements

You need an access-token for the phabricator instance.
This is supplied by putting a proper `.arcrc` file in the homedirectory of the user.

It is recommended to use a virtualenv for the project:

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Before using, copy `.env.dist` to `.env` and adjust to your needs.


# From Phabricator to Gitea-ready files

To prevent having to deal with tons of parameters, the (main) tool has been written as a multi-call binary; meaning that it recognizes its function based on its name. This allows you to use symlinks for each new function.

| Name                  | function                                                                        |
|-----------------------|---------------------------------------------------------------------------------|
| pt.py                 | Main binary; not called directly.                                               |
| pt.dump               | Stub; future purpose                                                            |
| pt.dump.maniphest     | This pulls all (new) maniphest tasks (issues) from Phabricator                  |
| pt.dump.maniphest.all | This pulls all maniphest tasks (issues) from Phabricator, in order of T-number. |
| pt.create.users       | Create Gitea users for the Phabricator users with an actual email address       |
| pt.convert            | Runs the conversion of Phabricator to Gitea data                                |
| pt.convert.maniphest  | Convert Tasks into Issues (convert/issues/\*.yaml)                              |

Run this to convert the Phabricator dump to Gitea files. Gitea must be running & reachable already.

```sh
./pt.create.users
./pt.convert
```

# Importing into Gitea

Run this to import everything into Gitea:

```sh
./test.sh
python import-all.py
```

If you want to import only a single repository, for example Flamenco, use
`python import-all.py flamenco`. Multiple repositories can be listed on the CLI.

# Resetting Gitea

While working on the port, it is sometimes useful to fully reset Gitea. For
this, use `reset-gitea.sh`.

**WARNING** update your `.env` file first. See `.env.dist` for an example.
