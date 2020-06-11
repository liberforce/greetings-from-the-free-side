#!/usr/bin/env bash

this_script=$(readlink -e "$0")
this_script_dir=$(realpath $(dirname "${this_script}"))

PYTHONPATH="${this_script_dir}" /usr/bin/env python -m blog2pelican.tool --markup markdown dotclear "$@"
