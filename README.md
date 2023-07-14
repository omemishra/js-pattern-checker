# js-pattern-checker
The tool scans domain URLs for JS files and detects sensitive patterns. Uses Wayback Machine API and requests for analysis.


## Usage

- Ensure you have Python 3 installed on your system.
- Save the code to a Python file (e.g., `js_sensitive.py`).
- Open a terminal or command prompt and navigate to the directory where the Python file is located.
- Run the code using the command `python js_sensitive.py <domain_urls>`, where `<domain_urls>` is a space-separated list of domain URLs to scan.

## Installation Instructions

- Ensure you have the required Python modules installed. You can install them using the following command:



- The code utilizes the `waybackurls` command-line tool. Ensure it is installed and accessible in your environment.
- Installation instructions for `waybackurls` can be found at: [https://github.com/tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)

**Note:** The `waybackurls` tool is used to fetch JavaScript files associated with the specified domain URLs from the Wayback Machine. Make sure the tool is installed and available in your system's PATH.

Once you have fulfilled the prerequisites and followed the usage instructions, the code will scan the provided domain URLs for JavaScript files and check for sensitive hardcoded patterns within them. The results will be printed to the console, indicating the presence of sensitive patterns and the corresponding files.

Please make sure to replace `<domain_urls>` in the usage instructions with the actual domain URLs you want to scan.

