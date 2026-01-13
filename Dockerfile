FROM python:3.12-slim
WORKDIR /app
COPY app/ .
RUN pip install flask
EXPOSE 8081
CMD ["python", "app.py"]
