#!/usr/bin/env python3
# thoth-package-analyzer
# Copyright(C) 2019 Fridolin Pokorny, Bissenbay Dauletbayev
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A command line interface for Python package analyzer used in project Thoth."""

import logging
import time

import click
from thoth.common import init_logging
from thoth.analyzer import print_command_result
from thoth.package_analyzer import __version__ as analyzer_version
from thoth.package_analyzer import __title__ as analyzer_name
from thoth.package_analyzer.python import PythonDigestsFetcher


init_logging()
_LOGGER = logging.getLogger(__name__)


def _print_version(ctx, _, value):
    """Print package-analyzer version and exit."""
    if not value or ctx.resilient_parsing:
        return
    click.echo(analyzer_version)
    ctx.exit()


@click.group()
@click.pass_context
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    envvar="THOTH_PACKAGE_ANALYZER_DEBUG",
    help="Be verbose about what's going on.",
)
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    callback=_print_version,
    expose_value=False,
    help="Print package analyzer version and exit.",
)
def cli(ctx=None, verbose=False):
    """Thoth package-analyzer command line interface."""
    if ctx:
        ctx.auto_envvar_prefix = "THOTH_PACKAGE_ANALYZER"

    if verbose:
        _LOGGER.setLevel(logging.DEBUG)

    _LOGGER.debug("Debug mode is on")
    _LOGGER.info("Version: %s", analyzer_version)


@cli.command()
@click.pass_context
@click.option(
    "--package-name",
    "-p",
    type=str,
    required=True,
    envvar="THOTH_PACKAGE_ANALYZER_PACKAGE_NAME",
    help="Package name for which digests should be fetched.",
)
@click.option(
    "--package-version",
    "-v",
    type=str,
    required=True,
    envvar="THOTH_PACKAGE_ANALYZER_PACKAGE_VERSION",
    help="Package version for which digests should be fetched.",
)
@click.option(
    "--index-url",
    "-i",
    type=str,
    required=False,
    default="https://pypi.org/simple",
    show_default=True,
    envvar="THOTH_PACKAGE_ANALYZER_INDEX_URL",
    help="URL of the Python package index to pull the package from.",
)
@click.option("--no-pretty", "-P", is_flag=True, help="Do not print results nicely.")
@click.option(
    "--output",
    "-o",
    type=str,
    envvar="THOTH_PACKAGE_ANALYZER_OUTPUT",
    default=None,
    help="Output file or remote API to print results to, in case of URL a POST request is issued.",
)
@click.option(
    "--dry-run",
    "-d",
    type=bool,
    default=False,
    show_default=True,
    help="Schedule a package analyzer job, do not send output to result-API.",
)
def python(
    click_ctx,
    package_name: str,
    package_version: str,
    index_url: str = None,
    no_pretty: bool = True,
    output: str = None,
    dry_run: bool = False,
):
    """Fetch digests for packages in Python ecosystem."""
    start_time = time.time()
    python_fetcher = PythonDigestsFetcher(index_url)
    result = python_fetcher.fetch(package_name, package_version)
    duration = start_time - time.time()

    print_command_result(
        click_ctx,
        result,
        analyzer=analyzer_name,
        analyzer_version=analyzer_version,
        output=output or "-",
        duration=duration,
        pretty=not no_pretty,
        dry_run=dry_run,
    )


if __name__ == "__main__":
    cli()
