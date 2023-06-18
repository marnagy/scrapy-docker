FROM python:3.10.10-bullseye

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir flask psycopg2-binary

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]