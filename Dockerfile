FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PORT=80
ENV CACHESRV="localhost:11211"
EXPOSE 80

COPY ./app /app
ENTRYPOINT ["python"]
CMD ["app.py"]
