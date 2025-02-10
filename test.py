from structured_data_extractor import SearchResultExtractor
import json

# Complete search results
search_results = {
    "organic_results": [
        {
            "position": 1,
            "title": "Elias Salvador Smidt Torjani (@eliastorjani)",
            "link": "https://www.instagram.com/eliastorjani/",
            "snippet": "Follow. This account is private. Already follow eliastorjani? Switch to the app or log in to see their photos and videos. Switch to the App.",
            "source": "Instagram"
        },
        {
            "position": 2,
            "title": "Elias torjani (eliastorjani) - Profile",
            "link": "https://dk.pinterest.com/eliastorjani/",
            "snippet": "See what Elias torjani (eliastorjani) has discovered on Pinterest, the world's biggest collection of ideas.",
            "source": "Pinterest"
        },
        {
            "position": 3,
            "title": "Salam bromigos and bromigas! 👋I'm a 21 year old boy from ...",
            "link": "https://www.instagram.com/activebulgariansociety/p/CM4CZWeFGkk/",
            "snippet": "Photo shared by Active Bulgarian Society on March 26, 2021 tagging @eliastorjani. ... eliastorjani · @activebulgariansociety @yungleth you.",
            "source": "Instagram"
        },
        {
            "position": 4,
            "title": "Sommerlejr / Summer Camp",
            "link": "https://www.icye.dk/en/summer-camp/",
            "snippet": "eliastorjani@gmail.com. Returning to the train station. When the camp ends on Saturday, the shared bus will again drive people back to Odense ...",
            "source": "Dansk ICYE",
            "date": "Aug 15, 2024"
        }
    ],
    "inline_images": [
        {
            "source": "https://www.icye.dk/en/summer-camp/",
            "title": "Sommerlejr / Summer Camp",
            "source_name": "Dansk ICYE"
        },
        {
            "source": "https://www.facebook.com/DanskICYE/posts/",
            "title": "Dansk ICYE - Hils på Dansk ICYE's bestyrelse 2024",
            "source_name": "Facebook"
        }
    ]
}

# Input Details --> in ABC now
    # name = input("Enter the person's name: ")
    # username = input("Enter their username: ")
#     target = Target()
#     dork = Dork()
#     # Step 1: Generate Queries --> in ABC now
#     print("\nGenerated Queries:")
#     dork.query_generator(dork.name, dork.username)
#     print(f"Queries from dork instance: {dork.queries}")
    
#     # Step 2: Perform Google Searches
#     g = GoogleManager()
#     urls = g.search(dork.queries)  # Pass queries from the dork instance
    
#     print("\nRetrieved URLs:")
#     print(urls)
# # Input Details --> in ABC now
#     # name = input("Enter the person's name: ")
#     # username = input("Enter their username: ")
#     target = Target()
#     dork = Dork()
#     # Step 1: Generate Queries --> in ABC now
#     print("\nGenerated Queries:")
#     dork.query_generator(dork.name, dork.username)
#     print(f"Queries from dork instance: {dork.queries}")
    
#     # Step 2: Perform Google Searches
#     g = GoogleManager()
#     urls = g.search(dork.queries)  # Pass queries from the dork instance
    
#     print("\nRetrieved URLs:")
#     print(urls)


# Input Details --> in ABC now
    # name = input("Enter the person's name: ")
    # username = input("Enter their username: ")
    # target = Target()
    # dork = Dork()
    # # Step 1: Generate Queries --> in ABC now
    # print("\nGenerated Queries:")
    # dork.query_generator(dork.name, dork.username)
    # print(f"Queries from dork instance: {dork.queries}")
    
    # # Step 2: Perform Google Searches
    # g = GoogleManager()
    # urls = g.search(dork.queries)  # Pass queries from the dork instance
    
    # print("\nRetrieved URLs:")
    # print(urls)
    # # # Step 3: Extract Text Content
    # extractor = TextExtractor()
    # content = extractor.extract_bulk(urls)
    # print(f"\nExtracted content from {len(content)} URLs.")
    #  # # Step 4: Save to File
    # output_file = "extracted_content.txt"
    # extractor.save_to_file(content, output_file)
    

if __name__ == "__main__":
    
    # Create extractor instance
    extractor = SearchResultExtractor(search_results)

    # Optionally fetch page contents (this may take a while)
    print("Fetching page contents...")
    extractor.fetch_page_contents()

    # Save to JSON file
    extractor.to_json('structured_data.json')

    print("Data has been extracted and saved to structured_data.json")
