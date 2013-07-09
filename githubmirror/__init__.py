# -*- encoding: utf-8 -*-
"""
A script that will mirror every repository in a Github organization locally.

Usage:
    github-mirror (init|sync) <organization> [options]

Options:
    --workdir=/path   Path to sync repositories to
    --only-repo=repo  Will only sync <org>/<repo> instead of every repo
"""
import os
import docopt

import main


def cmd():
    args = docopt.docopt(__doc__)

    dir = args['--workdir']
    if not dir:
        dir = os.getcwd()

    org = main.get_organization(args['<organization>'], dir)
    if args['--only-repo']:
        repos = [org.get_repo(args['--only-repo'])]
    else:
        repos = org.get_repos()

    if args['init']:
        main.init_repos(repos, dir)

    main.fetch(repos, dir)

if __name__ == '__main__':
    cmd()
