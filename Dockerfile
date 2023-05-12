FROM python:3.11.3-alpine
WORKDIR /app
EXPOSE 8000

ADD . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["--bind", ":8000", "app:app"]