# backend/Dockerfile

# Stage 1: Build dependencies (if you have C extensions that need compiling)
FROM python:3.9-slim as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for psycopg2 and PostGIS client utilities
# and potentially other libraries like Pillow (for images) or lxml
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libgdal-dev \
    gdal-bin \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*
    # For PostGIS client utilities (like shp2pgsql, raster2pgsql), though not strictly needed for app runtime
    # postgresql-client \
    # For Pillow (image processing)
    # libjpeg62-turbo-dev zlib1g-dev libtiff-dev libfreetype6-dev liblcms2-dev libwebp-dev \
    # For GDAL (if djangorestframework-gis needs it for more complex operations, or if you use django.contrib.gis.gdal)
    # libgdal-dev \
    # For GEOS and PROJ (core GIS libraries, usually libpq-dev pulls some of this)
    # libgeos-dev libproj-dev \

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Stage 2: Final application image
FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PYTHONPATH=/app

# Install system dependencies (minimal set for runtime)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libgdal32 \
    gdal-bin \
    && rm -rf /var/lib/apt/lists/*
    # libgdal30 # If using GDAL features from django.contrib.gis.gdal
    # libgeos-c1v5 # If needed by GEOS features
    # libproj19 # If needed by PROJ features

# Copy pre-built wheels and install
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt

# Create a non-root user to run the application
RUN groupadd -r django && useradd -r -g django django
RUN mkdir -p /app/staticfiles /app/mediafiles && \
    chown -R django:django /app

# Copy application code
COPY . .
RUN python manage.py collectstatic --noinput --clear
RUN mkdir -p /app/staticfiles && \
    chown -R django:django /app/staticfiles
USER django

# Expose the port Gunicorn will run on
EXPOSE 8002

# Entrypoint script for migrations and running Gunicorn (see backend/entrypoint.sh below)
# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8002", "--workers", "3"]
# Using an entrypoint script is better for running migrations first