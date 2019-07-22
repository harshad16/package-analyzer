#!/usr/bin/env sh
#
# This script is run by OpenShift's s2i. Here we guarantee that we run desired
# sub-command based on env-variables configuration.
#

case $THOTH_PACKAGE_ANALYZER_SUBCOMMAND in
	'python')
		exec /opt/app-root/bin/python3 thoth-package-analyzer python
		;;
	*)
		echo "Application configuration error - no analyzer subcommand specified." >&2
		exit 1
		;;
esac