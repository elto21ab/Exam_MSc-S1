from googlesearch import search
import requests
from typing import List, Dict

class Target():
    NAME = input("Name? ")
    USERNAME = input("Username? ")
    QUERIES = []
    URLS = []

def sanity(self):
    print(f"Name: {Target.NAME}\n"
          f"Username: {Target.USERNAME}\n"
          f"queries: {Target.QUERIES}\n"
          f"urls: {Target.URLS}")

def rm_dublicates(self):
    # Remove dublicates from any list
    self.URLS = list(set(self.URLS))
    print(f"urls: {self.URLS}")


class Dork(Target):
    def __init__(self):
        pass

    def query_generator(self, NAME: str, USERNAME: str) -> str:
        """Generates a Google dorking queries."""
        google = f'"{NAME}"'
        fb = f'site:facebook.com intext:"{USERNAME}"'
        fb_name = f'site:facebook.com intext:"{NAME}"'
        ig = f'site:instagram.com intext:"{USERNAME}"'
        
        self.QUERIES.extend([google, fb, fb_name, ig])
        print(f"Queries: {self.QUERIES}\n")
        return google, fb, ig, fb_name

class GoogleManager(Target):
    def __init__(self):
        pass

    def search(self, QUERIES: List[str], URLS: List[str]) -> List[str]:
        for i, query in enumerate(QUERIES):
            print(f"Processing query {i + 1}/{len(QUERIES)}: {query}")
            results = list(search(query))
            self.URLS.extend(results)

        rm_dublicates(URLS)
        return results


# -----------------------------
# Main Workflow
# -----------------------------
if __name__ == "__main__":
    # Input Details --> in ABC now
    # name = input("Enter the person's name: ")
    # username = input("Enter their username: ")

    # Step 1: Generate Queries --> in ABC now
    # DorkGenerator().single_query(NAME)
    # DorkGenerator().multi_query(NAME, USERNAME)
    # print("\nGenerated Queries:")
    # print(DorkGenerator.queries)


    # Step 2: Perform Google Searches
    g = GoogleManager()
    urls = g.search(queries)
    print("\nRetrieved URLs:")
    print(urls)

    # # Step 3: Extract Text Content
    # extractor = TextExtractor()
    # content = extractor.extract_bulk(urls)
    # print(f"\nExtracted content from {len(content)} URLs.")

    # # Step 4: Save to File
    # output_file = "extracted_content.txt"
    # extractor.save_to_file(content, output_file)

