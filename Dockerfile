FROM python:3.11 AS base

# Setting Services to be working directory
WORKDIR /Services

# Install Minio and Flask
RUN pip install --no-cache-dir minio flask

# Copy the current directory contents into the container at /Services
COPY ./Services /Services

# **  Login Service  **
FROM base AS login_service

CMD ["python", "Login.py"]

EXPOSE 5000

# ** Minio Service **

FROM base AS minio_service

CMD ["python", "Minio.py"]

EXPOSE 5000

FROM quay.io/minio/minio:latest AS minio-deployment_service

CMD ["server", "/data", "--console-address", ":9001"]

EXPOSE 9000 9001

# ** Purchase Service **

FROM base AS purchase_service

CMD ["python", "Purchase.py"]

EXPOSE 5000