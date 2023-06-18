from time import sleep 
from sys import stdout
import psycopg2


connection = psycopg2.connect(
    host = 'host.docker.internal',
    port = 5432,
    user = 'admin',
    password = 'scrapy_task',
    database = 'sreality'
)
curr = connection.cursor()


for i in range(10):
    sleep(2)
    print(f'Hello from docker! - {i}')
    stdout.flush()