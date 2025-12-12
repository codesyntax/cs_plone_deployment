#!/bin/bash

set -e

export PYTHONIOENCODING=utf8
if [[ "$1" == *".py" ]] ; then
	if [ -f "$1" ]; then
	    echo "> Found python script '$1' as argument, will now run it"
	    python3 $@
	fi
fi
if [[ "$1" == *".sh" ]]; then
	if [ -f "$1" ]; then
	    echo "> Found bash script '$1' as argument, will now run it"
	    exec $@
	fi
fi

