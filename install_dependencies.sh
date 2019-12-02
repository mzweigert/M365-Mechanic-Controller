#!/bin/bash

PROJECT_DIR=$1

install_apps_if_not_exists() {
  for var in "$@"; do
    dpkg-query --show "$var"
    if [ $? -eq 1 ]; then
      echo "$var is not installed..."
      sudo apt-get -y install "$var"
    fi
  done
}

install_python_module_if_not_exists() {
  for var in "$@"; do
    python3 -c "import $var"
    if [ "$?" -eq 1 ]; then
      sudo pip3 install "$var"
    fi
  done
}
# PROJECT MANAGEMENT
install_apps_if_not_exists git python3-pip
# GPIO
install_apps_if_not_exists python3-rpi.gpio
# OLED DISPLAY LIB
install_apps_if_not_exists python3-dev python3-setuptools
install_apps_if_not_exists libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev tcl8.5-dev tk8.5-dev
install_python_module_if_not_exists Pillow adafruit_circuitpython_ssd1306
# PROJECT LIBS
install_python_module_if_not_exists click asyncio bleak

if [ ! -d "$PROJECT_DIR" ]; then
    mkdir "$PROJECT_DIR"
    command cd "$PROJECT_DIR"
    mkdir lib
fi

command cd "$PROJECT_DIR"/lib

if [ ! -d "py9b" ]; then
  git clone https://github.com/mzweigert/py9b
else
  command cd py9b
  git pull
  cd ..
fi
