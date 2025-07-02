#!/bin/bash
set -e
virtualenv virtualenv # Create a virtual environment named 'virtualenv'
source virtualenv/bin/activate # Activate the virtual environment
pip install -r requirements.txt --target virtualenv/lib/python3.9/site-packages
