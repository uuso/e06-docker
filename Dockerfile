FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8080

COPY ./app /app
CMD ["python" "app.py"]
