import argparse
import logging
from utils import extract_urls_from_query, is_valid_url
from scraper import scrape_company_data
from output import save_json, save_csv

logging.basicConfig(level=logging.INFO)

def run(query=None, urls=None):
    targets = extract_urls_from_query(query) if query else urls
    results = []

    for url in targets:
        if not url.startswith("http"):
            url = "http://" + url

        if not is_valid_url(url):
            logging.warning(f"Unreachable: {url}")
            continue

        logging.info(f"Scraping: {url}")
        data = scrape_company_data(url)
        if data:
            results.append(data)

    if results:
        save_json(results, "output/results.json")
        save_csv(results, "output/results.csv")
        logging.info(f"Saved {len(results)} records.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="Search query like 'fintech startups in India'")
    parser.add_argument("--urls", nargs="+", help="Direct URLs to scrape")

    args = parser.parse_args()
    run(args.query, args.urls)
