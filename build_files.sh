#!/bin/bash

# Pastikan pip terinstal dan terbaru
python -m pip install --upgrade pip

# Instal semua dependensi
python -m pip install -r requirements.txt

# Jalankan collectstatic
python manage.py collectstatic --noinput --clear

# Jalankan migrasi database
python manage.py migrate