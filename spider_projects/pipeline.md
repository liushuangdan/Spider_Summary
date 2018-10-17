
pipeline的代码，将item传过来的数据保存在数据库中
===

```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from projects.mysqlhelper import MysqlHelper

class ProjectsPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):
    def __init__(self):
        self.helper = MysqlHelper()

    def process_item(self, item, spider):
        insert_sql, data = item.get_insert_sql()
        self.helper.execute_modify_sql(insert_sql, data)
        return item

```








