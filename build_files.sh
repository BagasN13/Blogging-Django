#!/bin/bash

# Pastikan pip terinstal dan terbaru
python3.12 -m pip install --upgrade pip

# Instal semua dependensi
python3.12 -m pip install -r requirements.txt

# Jalankan collectstatic
python3.12 manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python3.12 manage.py migrate