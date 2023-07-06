FROM mcr.microsoft.com/playwright/python:v1.35.0-jammy

WORKDIR /docker_practice

COPY . /docker_practice

RUN pip install -r requirements.txt && playwright install chromium

CMD ["pytest", "test_docker.py"]