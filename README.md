>Exam code in the course 'Programming, Algorithms and Data Structures (CDSCO2402E)'

# OSINT Web Scraper

This repository contains Python scripts for Open Source Intelligence (OSINT) gathering, focused on automating web searches and content extraction to collect information about individuals.

## Features
*   **Automated Google Dorking:** Generates Google search queries (dorks) based on a target's name and username to find relevant online information.
*   **Multiple Search Methods:** Supports searching via:
    *   Standard Google Search (using `googlesearch-python` library - may be less reliable and prone to blocking).
    *   SerpAPI ([serpapi.com](https://serpapi.com/)) for more reliable and scalable search results.
    *   Google Custom Search Engine (CSE) API (requires API key and CSE ID).
*   **Content Extraction:** Extracts text content from webpages found in search results using the `requests` library.
*   **Data Output:** Saves extracted content to a text file, organized by URL.

## Setup

### Prerequisites

*   Python 3.7+
*   Pip package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You may need to create a `requirements.txt` file listing dependencies like `googlesearch-python`, `requests`, `serpapi-python` if it doesn't exist. Example `requirements.txt` content:*
    ```
    googlesearch-python
    requests
    serpapi-python
    google-api-python-client # Required for Google CSE API
    ```
    *)*

### API Key Configuration

For more reliable and scalable search results, I recommend to use either SerpAPI or Google Custom Search Engine API.

## Usage
Run the `test2.py` script from your terminal:

**Script Behavior:**
1.  The script will prompt you to enter a **name** and **username** for the target. *(Currently hardcoded in the script, you may need to modify `Target` class in `test2.py` to re-enable input prompts)*
2.  It generates Google dorking queries based on the provided information.
3.  It performs Google searches using the `search` function (default Google search without API). *(You can modify the `Google` class and `if __name__ == "__main__":` block in `test2.py` to use `serp_search` or `google_search` functions if you have configured API keys)*
4.  It extracts content from the URLs found.
5.  It saves the extracted content to a file named `[username]_extracted_content.txt` in the same directory.

**Customization:**
*   **Search Queries:**  Edit the `Dork.query_generator` method in `test2.py` to add, remove, or modify the generated search queries.
*   **Search Method:**  To use SerpAPI or Google CSE API, you'll need to:
    1.  Configure API keys as described in "API Key Configuration".
    2.  Modify the `Google` class and the `if __name__ == "__main__":` block in `test2.py` to call the `serp_search` or `google_search` methods instead of the default `search` method.  You'll need to pass your API keys to these functions.

## Disclaimer
*   This script is for educational and research purposes only.
*   Use responsibly and ethically. Respect privacy and terms of service of websites.
*   Be aware of limits when using search engines (with, or without APIs). Using SerpAPI or Google CSE API is recommended.
*   The accuracy and completeness of the gathered information is highly dependent on the target's online presence.

---
