# Taskfile

A Taskfile is a Utility file that allows to run task to simplify the execution of common tasks.

See [Github Repo](https://github.com/adriancooney/taskfile).

## Enable

To enable the `run` commands, you need to add this into your `.bash_profile` or `.zshrc` if using **zsh**.

```
alias run=./Taskfile
```

## Commands

The current task added are the following:

### Help

```
run help
```

This command returns all the main task included in the Taskfile

### Env

This command creates a new **virtual environment** with all the requirements with the desired python version and installs all the requirements

### Install Fnds

Installs the foundations tool for developers

```
run install-fnds
```

### Install

Runs `install-fnds` and `env`, so is ideal to setup an environment from start.

### Upgrade Packages

Upgrades all libraries in the `requirements.txt` over the project that are declared in the `requirements.in` files.

```
run upgrade-packages
```
