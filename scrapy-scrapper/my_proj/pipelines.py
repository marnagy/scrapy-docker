# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2
import os


class MyProjPipeline:
    def process_item(self, item, spider):
        return item

class PostgreSQLPipeline:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = os.getenv("POSTGRES_HOST"),
            port = os.getenv("POSTGRES_PORT"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD"),
            database = 'sreality'
        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_to_db(item)
        return item

    def store_to_db(self, item):
        print(f"Saving {item} to DB")
        try:
            self.curr.execute(""" insert into sreality_items (id, title, img_url) values (%s, %s, %s)""",
                            (
                                item['id'],
                                item['title'],
                                item['img_url']
                            )
                            )
            self.connection.commit()
            print(f"{item} saved.")
        except BaseException as e:
            print(e, item)
            print(f"Saving of item {item} FAILED.")
