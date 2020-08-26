FROM python:3.7
WORKDIR /app
COPY ./app /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PORT 5001
ENV CACHESRV "cachesrv-inner:11211"
ENTRYPOINT ["python"]
CMD ["app.py"]
