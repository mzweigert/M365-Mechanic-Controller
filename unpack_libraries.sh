#!/bin/bash

PROJECT_DIR=$1

if [ ! -d "$PROJECT_DIR/lib" ]; then
    mkdir -p "$PROJECT_DIR/lib"
fi

command cd "$PROJECT_DIR"/lib

if [ ! -d "py9b" ]; then
  git clone https://github.com/mzweigert/py9b
  command cd py9b
  cp -r py9b "$PROJECT_DIR"/src/
else
  command cd py9b
  git pull
  cp -r py9b "$PROJECT_DIR"/src/
  cd ..
fi
