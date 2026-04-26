# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class SP500CompanyItem(Item):
    ticker = Field()
    company = Field()
    sector = Field()
    sub_industry = Field()
    headquarters = Field()
    date_added = Field()
    cik = Field()
    founded = Field()

class RevenueItem(Item):
    rank = Field()
    company = Field()
    industry = Field()
    revenue_usd_m = Field()
    profit_usd_m = Field()
    employees = Field()
    country = Field()