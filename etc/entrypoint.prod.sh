#!/bin/bash

set -e

chmod +x ./etc/wait-for-it.sh
./etc/wait-for-it.sh $DB_PORT_5432_TCP_ADDR:5432 -- echo "postgres is up"

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py create_admin
python manage.py create_test_user

exec "$@"
