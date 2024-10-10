#!/bin/bash

# Set script to exit on error
set -e

echo "Creating environment namespaces..."

kubectl create namespace dev
kubectl create namespace staging
kubectl create namespace prod

echo "Namespaces created: dev, staging, prod"
