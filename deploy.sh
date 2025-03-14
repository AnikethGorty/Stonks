#!/bin/bash

# Update package list and install Python3 and pip if not already installed
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Run your Python app (replace 'app.py' with your main script)
python3 stonksml.py

chmod +x deploy.sh