from structured_data_extractor import SearchResultExtractor
import json

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
