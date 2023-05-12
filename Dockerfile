FROM python:3.11.3-bullseye
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "--bind 0.0.0.0:5000", "wsgi:app"]