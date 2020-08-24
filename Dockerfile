FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PORT=8080
EXPOSE 8080

COPY ./app /app
ENTRYPOINT ["python"]
CMD ["app.py"]
