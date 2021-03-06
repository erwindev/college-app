#!/bin/bash

source env.dev

# Check if rabbit and redis are up and running before starting the service.

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done

# Run the service

nameko run --config config.yml app.service --backdoor 3000