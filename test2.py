from googlesearch import search
import requests
from typing import List

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
    def search(self) -> List[str]:
        for i, query in enumerate(self.queries):
            print(f"Processing query {i + 1}/{len(self.queries)}: {query}")
            results = list(search(query))
            self.urls.extend(results)
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
            print(f"Error extracting from {url}: {e}")
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