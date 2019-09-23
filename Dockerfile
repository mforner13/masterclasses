FROM python:3.7.3
COPY ./app /code/app
COPY requirements.txt /code/
COPY masterclasses.py /code/
COPY migrations /code/migrations
COPY config.py /code/config.py
WORKDIR /code
CMD ["ping", "google.com"]
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=masterclasses.py
ENTRYPOINT flask run --host 0.0.0.0