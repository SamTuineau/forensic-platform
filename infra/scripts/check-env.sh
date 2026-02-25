#!/bin/sh

echo "Checking environment..."

docker --version
docker compose version

if [ $? -ne 0 ]; then
  echo "Docker not available"
  exit 1
fi

echo "Docker OK"