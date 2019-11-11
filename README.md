# Sty Documentation Website

## Description

This repo contains [sty](https://github.com/feluxe/sty)'s documentation website: http://sty.mewo.dev

The documentation website is build with sphinx.

## Developing / Writing Docs

You find the documentatio source in the `./sphinx` directory.

Run these commands to setup the project on your machine:

```
$ git clone https://github.com/feluxe/sty-docs.git
$ cd sty-docs
$ pipenv install --dev
```

The build script comes with a small command line interface, which you can access like this:

```
$ pipenv run python make.py
```

Run this command to get further information:

```
$ pipenv run python make.py --help
```
