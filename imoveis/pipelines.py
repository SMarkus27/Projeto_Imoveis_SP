import mysql.connector
from itemadapter import ItemAdapter


class OlxPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='user',
            passwd='passwd',
            database='olx_crawl_db'
            )

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS olx_crawl""")
        self.curr.execute("""create table olx_crawl(
                        category text,
                        bathrooms text,
                        type_house text,
                        size text,
                        bedrooms text,
                        garage text,
                        district text,
                        city text,
                        price text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        self.curr.execute(f"""INSERT INTO olx_crawl VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",list((
            item['category'],
            item['bathrooms'],
            item['type_house'],
            item['size'],
            item['bedrooms'],
            item['garage'],
            item['district'],
            item['city'],
            item['price'],


                ))
        )

        self.conn.commit()
        