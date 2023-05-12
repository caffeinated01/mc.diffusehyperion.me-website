FROM python:3.11.3-bullseye
WORKDIR /app
EXPOSE 5000

ADD . /app
RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["--bind", "--bind 0.0.0.0:5000", "wsgi:app"]