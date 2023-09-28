#!/bin/bash

echo "Installing requirements..."
pip install -r requirements.txt || { echo "Installing requirements failed" ; exit 1; }

echo "Starting server..."
python app.py &

echo "Opening website..."
sleep 2
xdg-open http://127.0.0.1:5000/ &

