from googlesearch import search
import requests
from typing import List
import json
import serpapi
from serpapi import GoogleSearch
import logging

# Add logging setup at the beginning of the file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Target:
    def __init__(self):
        self.name = "Elias Torjani"  #input("Name? ")
        self.username = "eliastorjani"  #input("Username? ")
        self.queries = []
        self.urls = []

    def sanity(self):
        print(f"Name: {self.name}\n"
              f"Username: {self.username}\n"
              f"queries: {self.queries}\n"
              f"urls: {self.urls}")

class Dork(Target):
    def query_generator(self):
        google = f'"{self.name}"'
        fb = f'site:facebook.com intext:"{self.username}"'
        fb_name = f'site:facebook.com intext:"{self.name}"'
        ig = f'site:instagram.com intext:"{self.username}"'

        self.queries.extend([google, fb, fb_name, ig])
        self.queries = list(set(self.queries))
        print(f"Queries: {self.queries}\n")
        return self.queries

class Google(Dork):
    def serp_search(query, api_key): # Serpapi
        params = {
            "q": query,
            "api_key": api_key
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        return [result.get('link') for result in results.get('organic_results', [])]
        # urls.extend(serp_search("foodclub", api_key))

    def google_search(query, api_key, cse_id): # Default Google w/ api
        from googleapiclient.discovery import build
        service = build("customsearch", "v1", developerKey=api_key)
        results = service.cse().list(q=query, cx=cse_id).execute()
        
        return [item['link'] for item in results.get('items', [])]
        # urls.extend(google_search("foodclub", api_key, cse_id))

    def search(self) -> List[str]: # Default Google w/o api
        for i, query in enumerate(self.queries):
            print(f"Processing query {i + 1}/{len(self.queries)}: {query}")
            results = list(search(query))
            self.urls.extend(results)
            # urls.extend(google_search("foodclub", api_key, cse_id))

            # try:
            #     results = list(search(query, num_results=5))
            #     print(f"Found {len(results)} results for query: {query}")
            #     self.urls.extend(results)
                # search_results = search(query, num_results=10)
                # Iterate through the generator and collect results
                # for url in search_results:
                #     print(f"Found URL: {url}")
                #     self.urls.append(url)
            # except Exception as e:
            #     print(f"Error during search for query '{query}': {e}")

    
        self.urls = list(set(self.urls))
        print(f"Total unique URLs found: {len(self.urls)}")
        print(f"URLs: {self.urls}\n")
        return self.urls

class Extractor(Google):
    def extract(self, url: str) -> str:
        """Extract content from a single URL."""
        try:
            response = requests.get("https://r.jina.ai/"+url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error extracting from {url}: {e}")
            return ""

    def extract_all_urls(self) -> List[str]:
        contents = []
        for url in self.urls:
            content = self.extract(url)
            if content:
                contents.append(content)
        return contents

    def save_contents(self, contents: List[str], filename: str = None):
        if filename is None:
            filename = f"{self.username}_extracted_content.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            for content in contents:
                f.write(f"{content}\n{'='*50}\n")


if __name__ == "__main__":
    e = Extractor()
    e.query_generator()
    e.search()
    contents = e.extract_all_urls()
    e.save_contents(contents)