import requests
from bs4 import BeautifulSoup
import re
from enrichment import detect_tech_stack
from urllib.parse import urlparse

EMAIL_RE = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PHONE_RE = r"(?:(?:\+?\d{1,3})?[ -]?)?(?:\(?\d{2,4}\)?[ -]?)?\d{3,4}[ -]?\d{3,4}"

def scrape_company_data(url):
    try:
        res = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, 'html.parser')
        text = soup.get_text(" ", strip=True)

        return {
            "company_name": soup.title.string.strip() if soup.title else "Unknown",
            "website": url,
            "emails": list(set(re.findall(EMAIL_RE, text))),
            "phones": list(set(re.findall(PHONE_RE, text))),
            "social_links": extract_socials(soup),
            "description": extract_description(soup),
            "address": extract_address(text),
            "tech_stack": detect_tech_stack(url)
        }
    except Exception as e:
        print(f"[ERROR] {url}: {e}")
        return None

def extract_socials(soup):
    socials = {}
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "linkedin.com" in href:
            socials["linkedin"] = href
        elif "twitter.com" in href:
            socials["twitter"] = href
        elif "facebook.com" in href:
            socials["facebook"] = href
    return socials

def extract_description(soup):
    desc = soup.find("meta", attrs={"name": "description"})
    return desc["content"].strip() if desc and desc.get("content") else ""

def extract_address(text):
    keywords = ["address", "location", "visit us at"]
    lines = text.splitlines()
    for line in lines:
        if any(k in line.lower() for k in keywords) and len(line) < 150:
            return line.strip()
    return ""
