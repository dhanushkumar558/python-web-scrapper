import subprocess
import json

def detect_tech_stack(url):
    try:
        result = subprocess.run(["wappalyzer", url], capture_output=True, text=True, timeout=15)
        parsed = json.loads(result.stdout)
        techs = [tech["name"] for tech in parsed.get("technologies", [])]
        return techs
    except Exception:
        return []
