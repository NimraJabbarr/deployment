#!/bin/bash
set -o errexit

pip install -r requirements.txt
python school_crm/manage.py migrate
python school_crm/manage.py collectstatic --noinput
