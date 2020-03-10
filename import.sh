#!/usr/bin/env bash

this_script=$(readlink -e "$0")
this_script_dir=$(realpath $(dirname "${this_script}"))

"${this_script_dir}/import.py" --dotclear --strip-raw -m markdown "$@"
