from googlesearch import search
import requests
from typing import List, Dict

class Target():
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

def rm_dublicates(self):
    # Remove dublicates from any list
    self.urls = list(set(self.urls))
    print(f"urls: {self.urls}")


class Dork(Target):
    def __init__(self):
        super().__init__()

    def query_generator(self) -> str: #, queries: List[str]) -> str:
        """Generates a Google dorking queries."""
        google = f'"{self.name}"'
        fb = f'site:facebook.com intext:"{self.username}"'
        fb_name = f'site:facebook.com intext:"{self.name}"'
        ig = f'site:instagram.com intext:"{self.username}"'
        
        self.queries.extend([google, fb, fb_name, ig])
        print(f"Queries: {self.queries}\n")
        return google, fb, ig, fb_name

class GoogleManager(Target):
    def __init__(self):
        pass

    def search(self, queries: List[str], urls: List[str]) -> List[str]:
        for i, query in enumerate(queries):
            print(f"Processing query {i + 1}/{len(queries)}: {query}")
            results = list(search(query))
            urls.extend(results)

        rm_dublicates(urls)
        return results

# -----------------------------
# Main Workflow
# -----------------------------
if __name__ == "__main__":
    # Input Details --> in ABC now
    # name = input("Enter the person's name: ")
    # username = input("Enter their username: ")
    target = Target()
    dork = Dork()
    # Step 1: Generate Queries --> in ABC now
    print("\nGenerated Queries:")
    dork.query_generator(dork.name, dork.username)
    print(f"Queries from dork instance: {dork.queries}")
    
    # Step 2: Perform Google Searches
    g = GoogleManager()
    urls = g.search(dork.queries)  # Pass queries from the dork instance
    
    print("\nRetrieved URLs:")
    print(urls)

    # # Step 3: Extract Text Content
    extractor = TextExtractor()
    content = extractor.extract_bulk(urls)
    print(f"\nExtracted content from {len(content)} URLs.")

    # # Step 4: Save to File
    output_file = "extracted_content.txt"
    extractor.save_to_file(content, output_file)
