# Sty Documentation Website

## Description

This repo contains the _source_ for [sty](https://github.com/feluxe/sty)'s documentation website: http://sty.mewo.dev

The website is created with a static-site-generator named [Sphinx](https://www.sphinx-doc.org).

The resulting builds are deployed via github-pages using this repo: https://github.com/feluxe/sty-docs-dist

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

Use this command to build the website:

```
$ pipenv run python make.py build
```

Open `./build/index.html` in your browser to see the result.
