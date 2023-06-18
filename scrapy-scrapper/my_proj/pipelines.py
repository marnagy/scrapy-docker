# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2


class MyProjPipeline:
    def process_item(self, item, spider):
        return item

class PostgreSQLPipeline:
    def __init__(self):
        self.connection = psycopg2.connect(
            host = '192.168.92.23',
            port = 5432,
            user = 'admin',
            password = 'scrapy_task',
            database = 'sreality'
        )
        self.curr = self.connection.cursor()

    def process_item(self, item, spider):
        self.store_to_db(item)
        return item

    def store_to_db(self, item):
        try:
            self.curr.execute(""" insert into sreality_items (id, title, img_url) values (%s, %s, %s)""",
                            (
                                item['id'],
                                item['title'],
                                item['img_url']
                            )
                            )
            self.connection.commit()
        except BaseException as e:
            print(e, item)
