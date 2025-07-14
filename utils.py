import requests
from googlesearch import search

def is_valid_url(url):
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        return r.status_code < 400
    except:
        return False

def extract_urls_from_query(query, limit=10):
    return list(search(query, num_results=limit))
