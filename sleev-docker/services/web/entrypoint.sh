#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$RELEASE" = "1" ]
then
    echo "Creating new db migration"
    flask db init
    flask db migrate -m $(date +"%Y-%m-%d_%H-%M")
    flask db upgrade
    echo "Migration finished"
fi

exec "$@"