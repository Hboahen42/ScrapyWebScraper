import scrapy

from financescraper.items import SP500CompanyItem

class SP500Spider(scrapy.Spider):
    name = "sp500"
    allowed_domains = ["en.wikipedia.org"]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "ROBOTSTXT_OBEY": True,
        "HTTPCACHE_ENABLED": False,
        "FEEDS": {
            "output/sp500_companies.json": {"format": "json", "indent": 2, "overwrite": True},
            "output/sp500_companies.csv": {"format": "csv", "overwrite": True},
        },
    }

    async def start(self):
        yield scrapy.Request(
            url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            callback=self.parse,
        )

    def parse(self, response):
        rows = response.css("table#constituents tbody tr")
        for row in rows:
            cols = row.css("td")
            if len(cols) < 8:
                continue

            item = SP500CompanyItem()
            item["ticker"] = cols[0].css("a::text").get("").strip()
            item["company"] = cols[1].css("a::text").get("").strip()
            item["sector"] = cols[2].css("::text").get("").strip()
            item["sub_industry"] = cols[3].css("::text").get("").strip()
            item["headquarters"] = cols[4].css("::text").get("").strip()
            item["date_added"] = cols[5].css("::text").get("").strip()
            item["cik"] = cols[6].css("::text").get("").strip()
            item["founded"] = cols[7].css("::text").get("").strip()

            yield item

