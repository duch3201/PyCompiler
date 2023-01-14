#!/bin/bash

# Create the PyC folder
mkdir PyC

# Change directory to PyC
cd PyC

# Download the files
if command -v wget > /dev/null; then
  wget https://github.com/yourusername/PyCompiler/PyC.py
  wget https://github.com/yourusername/PyCompiler/logger.py
  wget https://github.com/yourusername/PyCompiler/Sample_config.json
elif command -v curl > /dev/null; then
  curl -O https://github.com/yourusername/PyCompiler/PyC.py
  curl -O https://github.com/yourusername/PyCompiler/logger.py
  curl -O https://github.com/yourusername/PyCompiler/Sample_config.json
else
  echo "Error: wget or curl is not installed. Please install one of them and try again."
  exit 1
fi

# Make the script executable
chmod +x PyC.py

# Ask the user if they want to add the script to PATH
read -p "Do you want to add PyC.py to PATH? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
  echo "Adding PyC.py to PATH..."
  echo 'export PATH="$PATH:$HOME/PyC"' >> ~/.bashrc
  source ~/.bashrc
fi

# Delete the installer script
rm -- "$0"
