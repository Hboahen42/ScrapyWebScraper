import json
import csv

with open("output/largest_companies_revenue.json") as f:
    data = json.load(f)

fixed = []
for row in data:
    ind = row["industry"]

    if ind.startswith("$"):
        # Save originals before overwriting
        original_industry  = ind
        original_revenue   = row["revenue_usd_m"]
        original_profit    = row["profit_usd_m"]
        original_employees = row["employees"]

        row["industry"]      = ""
        row["revenue_usd_m"] = original_industry   # was in industry slot
        row["profit_usd_m"]  = original_revenue    # was in revenue slot
        row["employees"]     = original_profit     # was in profit slot
        row["country"]       = original_employees  # was in employees' slot

    fixed.append(row)

# Forward-fill country
last_country = ""
for row in fixed:
    if row["country"] and row["country"] != "[":
        last_country = row["country"]
    else:
        row["country"] = last_country

# Forward-fill industry
last_industry = ""
for row in fixed:
    if row["industry"]:
        last_industry = row["industry"]
    else:
        row["industry"] = last_industry

# Strip symbols
for row in fixed:
    for field in ["revenue_usd_m", "profit_usd_m"]:
        row[field] = row[field].replace("$", "").replace(",", "").strip()
    row["employees"] = row["employees"].replace(",", "").strip()

with open("output/largest_companies_revenue.json", "w") as f:
    json.dump(fixed, f, indent=2)

fields = ["rank", "company", "industry", "revenue_usd_m", "profit_usd_m", "employees", "country"]

with open("output/largest_companies_revenue.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(fixed)

print(f"Done. {len(fixed)} rows written to JSON and CSV")