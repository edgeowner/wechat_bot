#!/bin/sh

# redirect stdout and stderr to files
exec >./log/stdout.log
exec 2>./log/stderr.log

# now run the requested CMD without forking a subprocess
exec "$@"
