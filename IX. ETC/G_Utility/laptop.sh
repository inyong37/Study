#! /usr/bin/bash

if [-d "/sys/class/power_supply" ]; then
  echo "I am LAPTOP!"
  # https://stackoverflow.com/questions/22180253/how-can-i-check-if-the-platform-is-laptop-or-desktop-on-ubuntu
fi
