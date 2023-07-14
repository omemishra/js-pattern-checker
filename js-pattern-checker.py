import sys
import subprocess
import re
import requests
from colorama import Fore
from urllib.parse import urlparse, unquote

def enumerate_js_files(domain_url):
    command = f"waybackurls {domain_url} | grep '.js'"
    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)
        js_files = output.splitlines()
        js_files = [js_file.strip() for js_file in js_files if js_file.strip()]
        print(js_files)
        return js_files
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:
            print("No JavaScript files found for the domain.")
            return []
        else:
            print(f"Error occurred while executing 'waybackurls' command: {e}")
            return []

def check_sensitive_credentials(js_url):
    response = requests.get(js_url)
    if response.status_code == 200:
        content = response.text

        # Add your own sensitive keywords/patterns here
        sensitive_patterns = ['password', 'secret_key', 'api_key', 'access_token', 'wordpress', 'to-indexed-object', 'internals']
        found_patterns = []

        for pattern in sensitive_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                found_patterns.append(pattern)

        if found_patterns:
            print(Fore.GREEN + "Sensitive / Hardcoded Patterns found:", ', '.join(found_patterns))
            return True

    return False

# Check if the domain URLs are provided as command-line arguments
if len(sys.argv) < 2:
    print("Please provide at least one domain URL as an argument.")
    sys.exit(1)

domain_urls = sys.argv[1:]


for domain_url in domain_urls:
    print("Scanning domain:", domain_url)
    js_files = enumerate_js_files(domain_url)

    if not js_files:
        sys.exit(1)

    for js_file in js_files:
        if check_sensitive_credentials(js_file):
            print(Fore.RED+ "Sensitive hardcoded credentials found in file:", js_file)
        else:
            continue
    print()  # Print a new line between different domains
