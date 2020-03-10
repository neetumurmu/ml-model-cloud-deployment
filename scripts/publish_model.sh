#!/bin/bash

# Building packages and uploading them to a Gemfury repository

PYPI_USERNAME=$PYPI_USERNAME
PYPI_PASSWORD=$PYPI_PASSWORD

set -e

DIRS="$@"
BASE_DIR=$(pwd)
SETUP="setup.py"

warn() {
    echo "$@" 1>&2
}

die() {
    warn "$@"
    exit 1
}

build() {
    DIR="${1/%\//}"
    echo "BASE DIRECTORY is $BASE_DIR"
    echo "Checking directory $DIR"
    cd "$BASE_DIR/$DIR"
    [ ! -e $SETUP ] && warn "No $SETUP file, skipping" && return
    PACKAGE_NAME=$(python $SETUP --fullname)
    echo "Package $PACKAGE_NAME"
    BASE_DIR=$(pwd)
    echo "BASE DIRECTORY is $BASE_DIR"
    python "$SETUP" sdist bdist_wheel || die "Building package $PACKAGE_NAME failed"
    python -m twine upload --repository-url https://test.pypi.org/legacy/ -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD" dist/*
}

if [ -n "$DIRS" ]; then
    for dir in $DIRS; do
        build $dir
    done
else
    ls -d */ | while read dir; do
        build $dir
    done
fi