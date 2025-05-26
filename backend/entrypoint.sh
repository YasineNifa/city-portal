#!/bin/sh

# backend/entrypoint.sh

echo "Waiting for PostgreSQL to be ready..."
# Use nc (netcat) if available, or a simple Python script
# This simple loop waits for the DB host and port to be accessible
# Adjust DB_HOST and DB_PORT if they are different
DB_HOST=${DB_HOST:-db} # Default to 'db' if not set
DB_PORT=${DB_PORT:-5432} # Default to '5432' if not set

# A more robust check would involve trying to connect with psql
# while ! nc -z $DB_HOST $DB_PORT; do
#   sleep 0.1
# done

# Python alternative for waiting (if nc is not in slim image)
python << END
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(('${DB_HOST}', ${DB_PORT}))
        s.close()
        break
    except socket.error as ex:
        print(f"PostgreSQL not ready yet ({ex}), retrying in 1 second...")
        time.sleep(1)
END

echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files (if you serve them via Django in dev, or for WhiteNoise)
# echo "Collecting static files..."
# python manage.py collectstatic --noinput --clear

# Start Gunicorn server
echo "Starting Gunicorn..."
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3} --timeout ${GUNICORN_TIMEOUT:-120}