from flask import Flask, render_template
import psycopg2
import os

app = Flask('SReality webserver')
connection = psycopg2.connect(
    host = os.getenv("POSTGRES_HOST"),
    port = 5432,
    user = os.getenv("POSTGRES_USER"),
    password = os.getenv("POSTGRES_PASSWORD"),
    database = 'sreality'
)
cursor = connection.cursor()

postgreSQL_select_Query = "SELECT * FROM sreality_items"

@app.get('/')
def index():
    cursor.execute(postgreSQL_select_Query)
    items = cursor.fetchall()
    items = [
        {'title': row[1], 'img_url': row[2]}
        for row in items
    ]
    return render_template(
        'index.html',
        items=items
        #items=[{'title': 'test text', 'img_url': 'xxx'} for _ in range(50) ]
    )

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)