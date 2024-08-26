#!/bin/bash

# install.sh
# Script to install all dependencies for the Tor-X CLI tool

echo "[+] Starting the installation process..."

# Update package lists
sudo apt-get update

# Install Tor
echo "[+] Installing Tor..."
sudo apt-get install -y tor

# Install Python 3 and pip
echo "[+] Installing Python3 and pip..."
sudo apt-get install -y python3 python3-pip

# Install Python dependencies
echo "[+] Installing Python dependencies..."
pip3 install requests stem spacy reportlab argparse

# Download and install Spacy language model
echo "[+] Installing Spacy language model..."
python3 -m spacy download en_core_web_sm

echo "[+] Installation complete. You're ready to use Tor-X."

exit 0
