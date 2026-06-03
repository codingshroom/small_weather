#!/bin/bash
cd && cd coding/small_weather
python -m venv .venv
source .venv/bin/activate
sudo pacman -S python-pip
pip install -r requirements.txt
