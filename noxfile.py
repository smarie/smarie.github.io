import logging

import nox  # noqa
from pathlib import Path  # noqa


gh_org = "smarie"
gh_repo = "smarie.github.io"


# set the default activated sessions, minimal for CI
nox.options.sessions = ["docs"]
nox.options.error_on_missing_interpreters = True
nox.options.reuse_existing_virtualenvs = True  # this can be done using -r
# if platform.system() == "Windows":  >> always use this for better control
nox.options.default_venv_backend = "virtualenv"
# os.environ["NO_COLOR"] = "True"  # nox.options.nocolor = True does not work
# nox.options.verbose = True

nox_logger = logging.getLogger("nox")
# nox_logger.setLevel(logging.INFO)  NO !!!! this prevents the "verbose" nox flag to work !


@nox.session(python="3.11")
def dev(session: nox.Session):
    """Convenience session to have all the tools to debug"""
    session.install("-r", "requirements/docs-requirements.txt")
    session.install("-r", "requirements/stats-requirements.txt")


@nox.session(python="3.11")
def docs(session: nox.Session):
    """Generates the doc and serves it on a local http server. Pass '-- build' to build statically instead."""
    session.install("-r", "requirements/docs-requirements.txt")

    # session.run("bib", "-b", "docs/bib/papers.bib")
    # session.run(*split("bib.py -b docs/bib/papers.bib -o docs/bib/papers.md"))

    if session.posargs:
        # use posargs instead of "serve"
        session.run("mkdocs", *session.posargs)
    else:
        session.run("mkdocs", "serve")


@nox.session(python="3.11")
def stats(session: nox.Session):
    """Updates the statistics about pypi."""
    session.install("-r", "requirements/stats-requirements.txt")

    # session.run("python", "stats/get_pypi_stats.py")
    session.run("python", "stats/plot_available_stats.py")


@nox.session(python="3.11")
def publish(session: nox.Session):
    """Deploy the docs+reports on github pages. Note: this rebuilds the docs"""

    # Install all requirements
    session.install("-r", "requirements/docs-requirements.txt")
    session.run("pip", "freeze")

    # possibly rebuild the docs in a static way (mkdocs serve does not build locally)
    session.run("mkdocs", "build")

    # publish the docs
    session.run("mkdocs", "gh-deploy")
