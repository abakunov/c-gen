#!/bin/bash

# Exit on error
set -e

# Define the installation directory and package name
PACKAGE_NAME="code_generator"

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip not found. Please install pip first."
    exit 1
fi

# Install setuptools if not already installed
echo "Checking for setuptools..."
pip show setuptools &> /dev/null || {
    echo "setuptools not found. Installing setuptools..."
    pip install setuptools
}

# Install the package
echo "Installing the $PACKAGE_NAME package..."
pip install .

# Confirm installation
if command -v c-gen &> /dev/null; then
    echo "Installation complete! You can now use 'c-gen' as a command."
else
    echo "Installation failed. Please check for errors above."
fi
