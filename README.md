# ScrapyWebScraper

A Scrapy-based web scraping project designed to extract financial data from Wikipedia. It currently includes spiders for the S&P 500 companies and the largest companies by revenue.

## Overview

This project uses the [Scrapy](https://scrapy.org/) framework to crawl Wikipedia pages and extract structured data.

### Targeted Data
- **S&P 500 Companies**: Ticker, Company Name, Sector, Sub-industry, Headquarters, Date Added, CIK, and Founded Year.
- **Largest Companies by Revenue**: Rank, Company Name, Industry, Revenue (USD M), Profit (USD M), Employees, and Country.

## Requirements

- Python 3.x
- Scrapy
- (Optional) IPython (configured as the default Scrapy shell)
- **Visualization Dependencies**: pandas, matplotlib, seaborn, notebook (for `scrapyViz.ipynb`)

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ScrapyWebScraper
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install scrapy
   # If you want to use the configured shell:
   pip install ipython
   ```

## Running the Spiders

Spiders are executed using the `scrapy crawl` command from the `financescraper/` directory (where `scrapy.cfg` is located).

### 1. S&P 500 Spider
Extracts the list of S&P 500 companies from Wikipedia.
```bash
cd financescraper
scrapy crawl sp500
```
**Outputs**:
- `financescraper/financescraper/spiders/output/sp500_companies.json`
- `financescraper/financescraper/spiders/output/sp500_companies.csv`

### 2. Revenue Spider
Extracts the list of largest companies by revenue from Wikipedia. 

**Note**: Wikipedia's table layout for this page sometimes causes data alignment issues. A post-processing script `fixtable.py` is provided to clean and fix the output.

```bash
cd financescraper/financescraper/spiders
scrapy crawl revenue
python fixtable.py
```
**Outputs**:
- `financescraper/financescraper/spiders/output/largest_companies_revenue.json`
- `financescraper/financescraper/spiders/output/largest_companies_revenue.csv`

## Visualization

The project includes a Jupyter Notebook for visualizing the scraped data.

- **Notebook**: `scrapyViz.ipynb`
- **Charts**: Generated in the `charts/` directory.

To run the visualization:
1. Ensure all dependencies are installed (`pip install -r requirements.txt`).
2. Open `scrapyViz.ipynb` in Jupyter or an IDE that supports notebooks.
3. Run the cells to generate analysis charts like "Top 15 Largest Companies by Revenue" and "Revenue vs Profit".

## Project Structure

```text
ScrapyWebScraper/
├── charts/                  # Generated visualization charts
├── financescraper/          # Scrapy project root
│   ├── scrapy.cfg           # Scrapy configuration file
│   └── financescraper/      # Project module
│       ├── items.py         # Item definitions (RevenueItem, SP500CompanyItem)
│       ├── pipelines.py     # Item processing pipelines
│       ├── settings.py      # Project settings (Throttling, User-Agent, etc.)
│       └── spiders/         # Spider implementations
│           ├── Revenue.py   # "revenue" spider
│           ├── SP500.py     # "sp500" spider
│           ├── fixtable.py  # Post-processing script for revenue data
│           └── output/      # Directory where scraped data is saved
├── scrapyViz.ipynb          # Data visualization notebook
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Environment Variables

- No specific environment variables are currently required. Configuration is managed via `financescraper/settings.py`.

## Scripts

- **Spider Execution**: Use `scrapy crawl <spider_name>`.
- **Data Fixing**: `financescraper/financescraper/spiders/fixtable.py` - Runs after the `revenue` spider to fix table alignment and format numeric values.