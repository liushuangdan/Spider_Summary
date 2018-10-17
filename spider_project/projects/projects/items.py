# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WeiboItem(scrapy.Item):
    username = scrapy.Field()
    text = scrapy.Field()
    created_at = scrapy.Field()
    attitudes_count = scrapy.Field()
    comments_count = scrapy.Field()
    reposts_count = scrapy.Field()
    add_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = 'INSERT INTO weibo_pro(username,created_at,text,attitudes_count,comments_count,reposts_count,add_time)' \
                     ' VALUES(%s,%s,%s,%s,%s,%s,%s)'
        data = (self['username'], self['created_at'], self['text'],self['attitudes_count'],self['comments_count'],self['reposts_count'],self['add_time'])
        return (insert_sql, data)

class LiepinItem(scrapy.Item):

    title = scrapy.Field()
    salary = scrapy.Field()
    position = scrapy.Field()
    experince = scrapy.Field()
    education = scrapy.Field()
    number = scrapy.Field()
    time_show = scrapy.Field()
    description = scrapy.Field()
    com_name = scrapy.Field()
    add_time = scrapy.Field()
    from_web = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = 'INSERT INTO job_zhaopin(title, salary, position, experince, education, number, time_show, description,add_time , from_web, com_name)' \
                     ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['title'], self['salary'], self['position'],self['experince'],self['education'],self['number'],self['time_show'],self['description'],self['add_time'],self['from_web'],self['com_name'])
        return (insert_sql, data)

class Weibo_twoItem(scrapy.Item):
    username = scrapy.Field()
    text = scrapy.Field()
    created_at = scrapy.Field()
    attitudes_count = scrapy.Field()
    comments_count = scrapy.Field()
    reposts_count = scrapy.Field()
    add_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = 'INSERT INTO weibo(username,created_at,text,attitudes_count,comments_count,reposts_count,add_time)' \
                     ' VALUES(%s,%s,%s,%s,%s,%s,%s)'
        data = (self['username'], self['created_at'], self['text'],self['attitudes_count'],self['comments_count'],self['reposts_count'],self['add_time'])
        return (insert_sql, data)




