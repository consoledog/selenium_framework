FROM --platform=linux/amd64 selenium/standalone-chrome:latest

USER root

# Install Python dependencies
COPY requirements.txt .
RUN pip install --break-system-packages -r requirements.txt

# Install Allure
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.24.1/allure-2.24.1.zip && \
    unzip -o allure.zip -d /opt/ && \
    if [ ! -f "/usr/bin/allure" ]; then ln -s /opt/allure-2.24.1/bin/allure /usr/bin/allure; fi && \
    rm -rf allure.zip

WORKDIR /app

COPY . .
