#!/bin/bash

set -e

library="$1"
temp_libs_dir="/temp_libs"
mkdir -p "$temp_libs_dir"

# Create a virtual environment
python3.8 -m venv venv
source venv/bin/activate

# Install the library and its dependencies
pip install --upgrade pip
pip install --no-cache-dir --target="$temp_libs_dir" "$library"

# Install numpy and its dependencies
pip install --no-cache-dir --target="$temp_libs_dir" numpy

# Deactivate the virtual environment
deactivate

# Remove unnecessary files
find "$temp_libs_dir" -type d -name "__pycache__" | xargs rm -rf
find "$temp_libs_dir" -type f -name "*.pyc" | xargs rm -f

# Create the zip file
output_zip="library_with_deps_${library}.zip"
(
    cd "$temp_libs_dir"
    find . -type f -print0 | xargs -0 zip "../$output_zip"
)

# Copy the zip file to the output folder
cp "$output_zip" /output/
