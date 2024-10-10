#!/bin/bash

if ! command -v helm &> /dev/null
then
    echo "Helm could not be found. Please install Helm."
    exit
fi

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo add postgres-operator-charts https://opensource.zalando.com/postgres-operator/charts/postgres-operator
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add minio-operator https://operator.min.io
helm repo update

# Install Ingress-NGINX Controller
helm install ingress-nginx ingress-nginx/ingress-nginx --namespace operators --create-namespace

# Install PostgreSQL Operator
helm install postgres-operator postgres-operator-charts/postgres-operator --namespace operators --create-namespace

# Install Prometheus (Monitoring)
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace

# Install Minio (Storage)
helm install operator minio-operator/operator --namespace operators --create-namespace

echo "Operators installed successfully."
