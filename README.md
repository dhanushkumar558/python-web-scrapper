# 🕵️‍♂️Python Scraper CLI Tool

A Python-based command-line tool that automates the discovery and extraction of company-related information from the web. Just provide a **search query** (e.g., "AI startups in India") or a list of **seed URLs**, and the tool will collect structured data like:

- Company Name  
- Website  
- Contact Info (Emails, Phone)  
- Social Profiles (LinkedIn, Twitter, etc.)  
- Tech Stack (via Wappalyzer)  
- Short Description / Tagline  
- Address or Location (basic)

---



## 🚀 What This Tool Does

| Feature                            | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| 🔍 **Google Search Integration**   | Uses `googlesearch-python` to extract URLs from a search query             |
| 🌐 **URL Validation**              | Checks reachability of URLs using `requests.head()`                        |
| 🧹 **HTML Parsing**                | Parses the HTML of the target website using `BeautifulSoup`               |
| 📧 **Contact Info Extraction**     | Detects emails and phone numbers with regex                               |
| 👤 **Social Profiles**             | Detects presence of LinkedIn, Twitter, Facebook, etc.                      |
| 🏢 **Company Overview**            | Tries to extract meta description, tagline, and physical address           |
| 💻 **Tech Stack Detection**        | Uses `Wappalyzer` CLI to detect technologies/frameworks used               |
| 🧾 **Structured Output**           | Saves all results in both `.json` and `.csv` formats to `/output`          |
| 🧠 **Extensible Architecture**     | Modular files make it easy to extend features like NLP, project extraction |

---



## 🏗️ How It Works (Internal Workflow)

1. **Input**:
   - You can either:
     - Provide a search query (e.g., `"cloud security companies in Singapore"`)
     - OR pass one or more company website URLs directly

2. **Discovery**:
   - If query is used: uses `googlesearch` to extract real company URLs
   - Each URL is validated using a lightweight HEAD request

3. **Scraping**:
   - Main page is fetched using `requests.get()`
   - HTML is parsed via `BeautifulSoup` to extract:
     - Page `<title>`
     - Meta tags
     - Links to social media
     - Text for email/phone/address matching

4. **Enrichment** (Optional):
   - Tech stack is extracted using `wappalyzer https://company.com` CLI command
   - Parsed from JSON and added to output

5. **Output**:
   - All results are saved into:
     - `output/results.json`
     - `output/results.csv`

---


✅ Features Breakdown


🟢 Level 1: Basic (Minimum Requirements)
Feature	Description
✅ Input Handling	Accepts a search query (--query) or list of seed URLs (--urls)
✅ URL Validation	Checks if URLs are well-formed and reachable using requests.head()
✅ Website Title Extraction	Scrapes the main <title> of the site to infer company name
✅ Email Extraction	Extracts emails using regex from visible site content
✅ Phone Number Extraction	Extracts phone numbers using regex
✅ JSON/CSV Output	Structured results saved to output/results.json and output/results.csv
✅ Error Handling	Gracefully handles unreachable sites or missing fields



🟡 Level 2: Medium (Enhanced Information Extraction)
Feature	Description
✅ Meta Description	Extracts <meta name="description"> tag for company tagline/summary
✅ Social Profiles	Detects LinkedIn, Twitter, Facebook URLs from the homepage
✅ Address/Location (Heuristic)	Extracts address using keyword heuristics like "Location", "Visit us at"
✅ Organized Output	Combines basic + medium fields into a single result object per company
✅ Modular Codebase	Separation of logic into scraper.py, utils.py, enrichment.py, etc.



🔵 Level 3: Advanced (Enriched & Intelligent)
Feature	Description
✅ Tech Stack Detection	Uses Wappalyzer CLI to list technologies
⚙️ Project Detection (Planned)	Crawl "About", "Projects", "Blog" pages to identify ongoing work
⚙️ Competitor Analysis (Planned)	Identify competitors via NLP on site content or external enrichment
⚙️ NLP Summary (Planned)	Use NLP models (spaCy / transformers) to generate brief profile summary
⚙️ API Enrichment (Planned)	Integrate Clearbit or Crunchbase for funding, location, industry data

🧠 Feature Summary Table
Category	Features Included
Basic	Query input, seed URLs, title, emails, phones, URL validation, error handling
Medium	Meta tags, social links, address detection, modular structure, CSV/JSON output
Advanced	Tech stack detection via Wappalyzer, optional future NLP/API integrations




## 🧪 Sample Output

CLI Prompt : "Game Developement startups in india"  

  CLI :   python main.py --query "game development startups in india" 


```json
{
    "company_name": "Top Game Development Companies in India | Indian Gaming Companies",
    "website": "https://www.juegostudio.com/blog/best-game-development-companies-in-india",
    "emails": [
      "info@juegostudio.com",
      "info.usa@juegostudio.com",
      "info.uk@juegostudio.com"
    ],
    "phones": [
      " 560 078",
      "+44 75 8784 0496",
      "+91 89298-0841",
      " 575006",
      "+1 (940)-2185249",
      "+966 50 269 7450"
    ],
    "social_links": {
      "facebook": "https://www.facebook.com/JuegoStudioPrivateLimited/",
      "twitter": "https://www.twitter.com/juegostudio",
      "linkedin": "https://www.linkedin.com/company/juego-studio"
    },
    "description": "Partner with one of India\u2019s leading game development companies to create engaging, cross-platform games with unique design and development solutions.",
    "address": "",
    "tech_stack": []
  }


📦 Output Details (Where & What Is Saved)

The tool automatically stores scraped company data in two formats:

Format	  File Name	          Location	                          Description
✅ CSV	results.csv	      output/ folder	             Easy to open in Excel, Sheets, etc.
✅ JSON	results.json	  output/ folder	         Structured data for programmatic usage

✅ Both files are automatically created after each successful run of the CLI.




🧰 Technology Stack
Purpose	Tool / Library
Web scraping	requests, beautifulsoup4
Query → URLs	googlesearch-python
Validation	requests.head()
Regex Matching	re
Tech Stack Enrich	Wappalyzer CLI
Output Serialization	json, csv


🧑‍💻 Setup Instructions
🔸 Step 1: Clone the Repo
bash
Copy
Edit
git clone <your-repo-url>
cd company_scraper
🔸 Step 2: Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
🔸 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you see externally-managed-environment error, use a virtualenv or pass --break-system-packages


You must have Node.js installed.



🧪 Usage Examples


📌 Use a Search Query
bash
Copy
Edit
python main.py --query "biotech startups in Europe"


📌 Use Specific URLs
bash
Copy
Edit
python main.py --urls https://example1.com https://example2.com
Results will be saved in:

output/results.json

output/results.csv



🧱 File Structure
graphql
Copy
Edit
company_scraper/
├── main.py             # CLI entry point
├── scraper.py          # HTML parsing and field extraction
├── enrichment.py       # Tech stack detection using Wappalyzer
├── utils.py            # URL validation, query → URLs
├── output.py           # Writers for JSON and CSV
├── requirements.txt
└── README.md



⚠️ Limitations & Notes
Detection of physical address, year, projects, etc. is best-effort and heuristic-based.

Wappalyzer requires Node.js & CLI access .

Google Search via googlesearch-python might block if overused (you can switch to SerpAPI or Bing API for scaling).

NLP project detection, funding data, or LinkedIn API integration can be added later as advanced extensions.



🌱 Future Enhancements
NLP-based project & competitor extraction from About pages

Funding/enrichment via Clearbit or Crunchbase API

GUI version with dashboard interface

Export to Excel or Google Sheets

Background scraping with queue handling (async)



🤝 Contribution & Customization
Feel free to fork, customize modules, or request advanced features like:

Semantic matching (NLP)

Web crawling beyond homepage

Django or Streamlit-based frontend for this tool



🧑 Author
Dhanush Kumar V.
MERN Stack Developer | Automation Enthusiast | Full Stack Problem Solver

Crafted with 💻 and ☕ for real-world web intelligence extraction


