FROM python:3.12-slim
WORKDIR /app
COPY log_system.py .
RUN mkdir -p /data
CMD ["python", "log_system.py"]
