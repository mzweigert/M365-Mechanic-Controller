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
install_apps_if_not_exists python3-dev python-smbus i2c-tools python3-pil python3-setuptools
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

if [ ! -d "Adafruit_Python_SSD1306" ]; then
  git clone https://github.com/adafruit/Adafruit_Python_SSD1306
  command cd Adafruit_Python_SSD1306
  sudo python3 setup.py install
else
  command cd Adafruit_Python_SSD1306
  git pull
  cd ..
fi
