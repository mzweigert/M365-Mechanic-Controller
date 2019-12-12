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

install_python_module_with_different_names_if_not_exists() {
    python3 -c "import $1"
    if [ "$?" -eq 1 ]; then
      sudo pip3 install "$2"
    fi
}

# PROJECT MANAGEMENT
install_apps_if_not_exists git python3-pip
# GPIO
install_apps_if_not_exists python3-rpi.gpio
# OLED DISPLAY LIB
install_apps_if_not_exists python3-dev python3-setuptools
install_apps_if_not_exists libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms1-dev libwebp-dev tcl8.5-dev tk8.5-dev
install_python_module_if_not_exists board
install_python_module_with_different_names_if_not_exists PIL Pillow
install_python_module_with_different_names_if_not_exists adafruit_ssd1306 adafruit-circuitpython-ssd1306

# PROJECT LIBS
install_python_module_if_not_exists click asyncio bleak

