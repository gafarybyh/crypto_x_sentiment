import asyncio
from config import setup_logging
from gemini import gemini_analyze
from tweet import search_tweets

# Setup Logging for first time run
setup_logging()


# TODO* MAIN
async def main():
    while True:
        # Get search query from user input
        search_query = input("\nEnter search query (e.g. #btc) or 'exit' to quit: ")
        
        # Check if user wants to exit
        if search_query.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
    
        # Get tweets with minimal 30 tweets
        list_of_tweets = await search_tweets(search_query=search_query, search_product="Top", minimum_tweets=30)
        
        # If tweets found, analyze tweets with Gemini
        if list_of_tweets:
            analyze_result = gemini_analyze(list_of_tweets, search_query)
        
            print(analyze_result)
        
        # Ask if user wants to continue
        continue_search = input("\nDo you want to search again? (y/n): ")
        if continue_search.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == '__main__':
    asyncio.run(main())
