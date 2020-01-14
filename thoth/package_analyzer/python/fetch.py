#!/usr/bin/env python3
# thoth-package-analyzer
# Copyright(C) 2019, 2020 Fridolin Pokorny, Bissenbay Dauletbayev
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

"""Fetch digests for packages in Python ecosystem."""

import logging

from thoth.python import Source
from thoth.package_analyzer.base import FetcherBase
from thoth.python.exceptions import NotFound

_LOGGER = logging.getLogger(__name__)


class PythonDigestsFetcher(FetcherBase):
    """Fetch digests of python package artifacts and all the files present in artifacts."""

    def __init__(self, index_url: str):
        """Initialize Python package analyzer."""
        self.source = Source(index_url)

    def fetch(self, package_name: str, package_version: str) -> dict:
        """Fetch digests of files present in artifacts for the given package."""
        _LOGGER.info(
            "Fetching digests for package %r in version %r from %r", package_name, package_version, self.source.url
        )

        error = False
        error_message = ""
        artifacts = []

        try:
            artifacts = self.source.get_package_hashes(package_name, package_version, True)
        except NotFound as exc:
            error = True
            error_message = str(exc)
            _LOGGER.warning(error_message)

        return {
            "package_name": package_name,
            "package_version": package_version,
            "index_url": self.source.url,
            "error": error,
            "error_message": error_message,
            "artifacts": artifacts,
        }
