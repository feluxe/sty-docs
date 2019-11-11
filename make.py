"""
Install:
  pipenv install --dev

Usage:
  make.py update src [<rev>]
  make.py build
  make.py deploy
  make.py -h | --help

Commands
  update src [<rev>]    This allows you to update sty's source files in `./sty`.
  build                 Run this command to build the sphinx docs. You find the result 
                        in `./build`. Open './build/index.html' to see the results in 
                        the browser.
  deploy                Push changes to the distribution repo 'feluxe/sty-docs-dist'.

Options:
  <rev>         Git revision from sty repo.
  -h, --help    Show this screen.
"""
import shutil
import os
import subprocess as sp
from cmdi import print_summary
from buildlib import git, wheel, project, yaml
from docopt import docopt
from sty import fg
import prmt
from distutils.dir_util import copy_tree
from glob import glob

proj = yaml.loadfile('Project')


class Cfg:
    version = proj['version']
    registry = 'pypi'


def _save_git_hash():
    r = sp.run(['git', 'rev-parse', 'HEAD'], cwd='sty', stdout=sp.PIPE)
    with open('sty_src_hash', 'w') as f:
        f.write(r.stdout.decode('utf-8'))


def update_src(rev):

    if not os.path.exists('sty/.git'):
        sp.run(['git', 'clone', 'https://github.com/feluxe/sty.git'])
    else:
        sp.run(['git', 'fetch', 'origin', 'master'], cwd='sty')

    sp.run(['git', 'checkout', rev or 'master'], cwd='sty')
    _save_git_hash()


def build(cfg: Cfg):

    # q = (
    #     f"{fg.red}WARNING{fg.rs}\n"
    #     "Documentation changes and code changes should use seperate commits.\n"
    #     "Only proceed if there are no uncommited code changes.\n\n"
    #     "Do you want to build the documentation pages?")
    # if not prmt.confirm(q, 'n'):
    #     return

    # Get sty's source

    with open('sty_src_hash', 'r') as f:
        rev = f.read()

    if not os.path.exists('sty/.git'):
        sp.run(['git', 'clone', 'https://github.com/feluxe/sty.git'])
        sp.run(['git', 'checkout', rev], cwd='sty')
    else:
        sp.run(['git', 'checkout', rev], cwd='sty')

    # Build Static Page with Sphinx

    sp.run(['make', 'html'], cwd='sphinx')

    build_html_dir = 'sphinx/_build/html'

    if os.path.isfile(f"{build_html_dir}/index.html"):
        shutil.rmtree('docs', ignore_errors=True)
        shutil.copytree(build_html_dir, 'docs')
        shutil.rmtree(build_html_dir, ignore_errors=True)
        shutil.copyfile('sphinx/CNAME', 'docs/CNAME')

    # Remove modernizer
    # This is needed to reduce flickering on page load until this is fixed:
    # https://github.com/readthedocs/sphinx_rtd_theme/issues/724

    for html_file in glob("./docs/**/*.html", recursive=True):
        print(html_file)
        data = ""
        with open(html_file, 'r') as fr:
            for line in fr:
                if 'modernizr.min.js"' not in line and \
                   'js/theme.js' not in line:

                    data += line

        with open(html_file, 'w') as fw:
            fw.write(data)


def deploy(cfg: Cfg):

    dist_repo_url = 'https://github.com/feluxe/sty-docs-dist.git'

    if not os.path.exists('dist/.git'):
        sp.run(['git', 'clone', dist_repo_url, 'dist'])
    else:
        sp.run(['git', 'remote', 'set-url', 'origin', dist_repo_url], cwd='dist')
        sp.run(['git', 'pull', 'origin', 'master'], cwd='dist')

    copy_tree('docs', 'dist')

    sp.run(['git', 'add', '-A'], cwd='dist')

    # TODO: Come up with a good commit message here:
    r = sp.run(['git', 'commit', '-m', 'new build'], cwd='dist', stdout=sp.PIPE)

    if 'nothing to commit' in r.stdout.decode('utf-8'):
        print("\nThere is nothing new to deploy.")
        return

    sp.run(
        [
            'git',
            'remote',
            'set-url',
            'origin',
            'git@github.com:feluxe/sty-docs-dist.git',
        ],
        cwd='dist'
    )

    sp.run(['git', 'push', 'origin', 'master'], cwd='dist')


def run():

    cfg = Cfg()
    args = docopt(__doc__)
    results = []

    if args['update'] and args['src']:

        results.append(update_src(args['<rev>']))

    if args['build']:
        results.append(build(cfg))

    if args['deploy']:
        results.append(deploy(cfg))

    if any(results):
        print_summary(results)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print('\n\nScript aborted by user.')
