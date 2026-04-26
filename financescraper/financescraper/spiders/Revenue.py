import scrapy

from financescraper.items import RevenueItem


class RevenueSpider(scrapy.Spider):
    name = "revenue"
    allowed_domains = ["en.wikipedia.org"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "ROBOTSTXT_OBEY": True,
        "HTTPCACHE_ENABLED": False,
        
        "FEEDS": {
            "output/largest_companies_revenue.json": {"format": "json", "indent": 2, "overwrite": True},
            "output/largest_companies_revenue.csv": {"format": "csv", "overwrite": True},
        },
    }

    async def start(self):
        yield scrapy.Request(
            url="https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue",
            callback=self.parse,
        )

    def parse(self, response):
        rows = response.css("table.wikitable tbody tr")
        for row in rows:
            cols = row.css("td")
            if len(cols) < 3:
                continue

            item = RevenueItem()
            item["rank"] = row.css("th::text").get("").strip()
            item["company"] = cols[0].css("a::text").get("").strip()
            item["industry"] = cols[1].css("::text").getall()[0].strip() if cols[1].css("::text").getall() else ""

            revenue_text = cols[2].css("::text").getall()
            item["revenue_usd_m"] = revenue_text[0].strip() if revenue_text else ""

            # get the profit
            item["profit_usd_m"] = cols[3].css("::text").get("").strip() if len(cols) > 3 else ""

            # get the employees
            item["employees"] = cols[4].css("::text").get("").strip() if len(cols) > 4 else ""

            # get the country
            item["country"] = cols[5].css("::text").get("").strip() if len(cols) > 5 else ""

            if item["company"]:
                yield item