#!/bin/bash
set -e

if [ "$#" -ne 0 ]; then
    exec "$@"
else
    for file in ftfbroker/protobuf/**/*.proto; do
        /protobuf/bin/protoc "$file" --python_out=. --mypy_out=.
    done
fi
