#!/bin/bash

mv os-install ../../usr/etc
mv os-installer ../../usr/bin
cd ..
cd ../usr/etc/apt
rm -rf sources.list.d
cd
apt-get update -y
apt-get upgrade -y
apt upgrade -y
pkg install proot-distro -y
cd os-installer
pkg install python -y

os-installer