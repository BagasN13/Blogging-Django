#!/bin/bash

# Exit on error
set -o errexit

# Pastikan pip terinstal dan terbaru
python3 -m pip install --upgrade pip

# Instal semua dependensi
python3 -m pip install -r requirements.txt

# Jalankan collectstatic
python3 mysite/manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python3 mysite/manage.py migrate