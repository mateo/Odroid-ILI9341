#!/bin/bash

# Instructions
#
# chmod a+x setup.sh
# ./setup.sh

# A significant amount of this script installs libgpiod, based on the legacy version of the script found here, and written by @makermelissa
# https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/libgpiod.sh



# INITIALIZE SPI

echo "Initializing SPI"
sudo modprobe spidev
sudo modprobe spi_s3c64xx

# Odroid XU4 should always initialize SPI as spidev1.0 every time
if [[ -e /dev/spidev1.0 ]]; then
	echo "Successfully initialized SPI"
	echo
else
	echo "Failed to initialize SPI, please do so manually"
	echo
fi

echo "Installing libgpiod dependencies"
echo

# Linux packages required for libgpiod
sudo apt-get install -y \
	autoconf \
	autoconf-archive \
	automake \
	build-essential \
	git \
	libtool \
	pkg-config \
	python3 \
	python3-dev \
	python3-setuptools \
	swig3.0 \
	wget

build_dir='mktemp -d /tmp/libgpiod.XXXX'
echo "Cloning libgpiod repository to $build_dir"
echo

cd "$build_dir"
git clone git://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git .
git checkout v1.4.2 -b v1.4.2 # Necessary since the newer versions of libgpiod require linux headers v5.5

echo "Building libgpiod"
echo

include_path=`python3 -c "from sysconfig import get_paths; print(get_paths()['include'])"`

export PYTHON_VERSION=3
./autogen.sh --enable-tools=yes --prefix=/usr/local/ --enable-bindings-python CFLAGS="-I/$include_path" \
   && make \
   && sudo make install \
   && sudo ldconfig

sudo cp bindings/python/.libs/gpiod.so /usr/local/lib/python3.?/dist-packages/
sudo cp bindings/python/.libs/gpiod.la /usr/local/lib/python3.?/dist-packages/
sudo cp bindings/python/.libs/gpiod.a /usr/local/lib/python3.?/dist-packages/


# Install the other relevant packages

echo "Installing Adafruit Blinka..."
echo
sudo pip3 install Adafruit-Blinka

echo "Installing Adafruit Circuitpython..."
echo
sudo pip3 install adafruit-circuitpython-rgb-display

echo "Installing Pillow..."
echo
sudo apt-get install -y python3-pil

echo "All done :)"
echo "Please test the installation by testing the board library:"
echo
echo "sudo python3"
echo "import board"
echo "dir(board)"
echo
echo "This should return an object containing a list of pinouts of the XU4"
echo
echo "Then run the test.py python script to test the LCD wiring"

exit 0
