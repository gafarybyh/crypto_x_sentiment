from twikit import Client, TooManyRequests, NotFound
import os
from datetime import datetime
from random import randint
import asyncio
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# X Account Environment Variables
USERNAME = os.getenv("USERNAME")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cookies_file = os.path.join(BASE_DIR, 'cookies.json')


# TODO* GET MULTIPLE PAGE TWEETS
async def get_multiple_pages_of_tweets(search_query: str = "#btc", search_product: str = "Top", min_tweets = 30):
    """
    Login X account and get multiple pages of tweets

    Args:
        search_query (str): Search query
        search_product (str): Search product (Top, Latest, Media)
        min_tweets (int): Minimum number of tweets to return

    Returns:
        list[Tweet]: List of tweets
    """
    all_tweets = []
    max_retries = 3  # Add retry limit
    retry_count = 0
    
    # Buat satu instance client yang akan digunakan untuk seluruh proses
    client = Client(language='en-US')
   
    
    #* LOGIN SEKALI DI AWAL
    try:
        # Check if cookies file exists and has content
        if os.path.exists(cookies_file) and os.path.getsize(cookies_file) > 0:
            # Load cookies from file
            client.load_cookies(cookies_file)
            print(f'{datetime.now()} - Successfully loaded cookies')
        else:
            # Login with credentials
            await client.login(
                auth_info_1=USERNAME,
                auth_info_2=EMAIL,
                password=PASSWORD
            )
            # Save cookies for future use
            client.save_cookies(cookies_file)
            print(f'{datetime.now()} - Login successful, cookies saved')
    except Exception as e:
        print(f'{datetime.now()} - Error during login: {str(e)}')
        return []
    
    #* GET FIRST PAGE TWEETS with max_entries
    while retry_count < max_retries:
        try:
            
            print(f'{datetime.now()} - Getting initial tweets...')
            
            tweets = await client.search_tweet(query=search_query, product=search_product, count=20)
            
            # Tambahkan tweets ke daftar
            for tweet in tweets:
                all_tweets.append(tweet)
            
            print(f'{datetime.now()} - Collected {search_product} {len(all_tweets)} tweets so far')
            
            #* GET NEXT PAGE TWEETS UNTIL min_tweets
            page_count = 1
            
            while len(all_tweets) < min_tweets:
                page_count += 1
                
                # Tambahkan jeda untuk menghindari rate limiting
                wait_time = randint(5, 10)
                print(f'{datetime.now()} - Waiting {wait_time} seconds before fetching page {page_count}...')
                await asyncio.sleep(wait_time)
                
                # Gunakan tweets.next() untuk mendapatkan halaman berikutnya
                try:
                    tweets = await tweets.next()
                    
                    if not tweets or len(tweets) == 0:
                        print(f'{datetime.now()} - No more tweets available')
                        break
                    
                    # Tambahkan tweets ke daftar
                    for tweet in tweets:
                        all_tweets.append(tweet)
                    
                    print(f'{datetime.now()} - Collected {search_product} {len(all_tweets)} tweets so far')
                    
                except TooManyRequests as e:
                    # Handle rate limiting specifically
                    wait_time = 120  # Default wait time of 2 minutes
                    if hasattr(e, 'rate_limit_reset') and e.rate_limit_reset:
                        # Calculate wait time based on rate limit reset if available
                        current_time = datetime.now().timestamp()
                        wait_time = max(e.rate_limit_reset - current_time + 5, 60)
                    
                    print(f'{datetime.now()} - Rate limit exceeded. Waiting {wait_time} seconds before retrying...')
                    await asyncio.sleep(wait_time)
                    continue
                except NotFound as e:
                    print(f'{datetime.now()} - 404 Not Found error: {str(e)}')
                    # If we get a 404, we might have an invalid cursor or the search is no longer valid
                    # Best to return what we have so far
                    break
                except Exception as e:
                    print(f'{datetime.now()} - Error fetching next page: {str(e)}')
                    # Tunggu lebih lama jika terjadi error
                    await asyncio.sleep(30)
                    continue
            
            # If we got here, we either collected enough tweets or ran out of pages
            break  # Exit the retry loop
        
        except TooManyRequests as e:
            wait_time = 120  # Default wait time of 2 minutes
            if hasattr(e, 'rate_limit_reset') and e.rate_limit_reset:
                current_time = datetime.now().timestamp()
                wait_time = max(e.rate_limit_reset - current_time + 5, 60)
            
            print(f'{datetime.now()} - Rate limit exceeded during initial fetch. Waiting {wait_time} seconds before retrying...')
            await asyncio.sleep(wait_time)
            retry_count += 1
            continue
        except NotFound as e:
            print(f'{datetime.now()} - 404 Not Found error during initial fetch: {str(e)}')
            # Try a different search approach or wait before retrying
            print(f'{datetime.now()} - Waiting 30 seconds before retry {retry_count+1}/{max_retries}...')
            await asyncio.sleep(30)
            retry_count += 1
            continue
        except Exception as e:
            print(f'{datetime.now()} - Error during tweet collection: {str(e)}')
            # Try again after a delay
            print(f'{datetime.now()} - Waiting 30 seconds before retry {retry_count+1}/{max_retries}...')
            await asyncio.sleep(30)
            retry_count += 1
            continue
    
    print(f'{datetime.now()} - Finished collecting {len(all_tweets)} tweets')
    return all_tweets

# TODO* SEARCH TWEET
async def tweets(search_query: str, search_product: str = "Top", minimum_tweets: int = 30) -> list[dict]:
    """
    Get tweets from Twitter based on search query

    Args:
        search_query (str): Search query (e.g., #BTC)
        search_product (str): Search product (Top, Latest, Media)
        minimum_tweets (int): Minimum number of tweets to return

    Returns:
        list[dict]: List of tweets
    """
    
    print(f'{datetime.now()} - Searching for tweets with query: {search_query}')
    
    all_tweets = await get_multiple_pages_of_tweets(search_query=search_query, search_product=search_product, min_tweets=minimum_tweets)
    
    if not all_tweets:
        print(f'{datetime.now()} - No tweets found for query: {search_query}')
        return []
    
    list_tweet = []
    
    for i, tweet in enumerate(all_tweets):
        tweet_count = i + 1 
        tweet_data = { 
            "tweet_count": tweet_count,
            "username": tweet.user.name,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweets": tweet.retweet_count,
            "favorites": tweet.favorite_count
        }
        
        list_tweet.append(tweet_data)
        
    return list_tweet


# TODO* ANALYZE WITH GEMINI
def get_gemini_response(data_to_analyze, query):
    """
    Get response from Gemini API

    Args:
        data_to_analyze (str): data to analyze
        query (str): query to search

    Returns:
        str: Response from Gemini API or error message
    """
    try:
        print(f'{datetime.now()} - Analyzing all tweets, please wait...')
        genai.configure(api_key=GEMINI_API_KEY)
        # gemini-2.5-flash-preview-04-17
        # gemini-2.0-flash
        model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
        prompt = f"""
        You are an expert crypto sentiment analyst focusing on **twitter sentiment** for crypto traders.

        Given a list of tweets about a cryptocurrency (e.g., Bitcoin), generate a concise, actionable sentiment report, focusing on whether there's an early momentum or notable sentiment shift.

        The report should contain:

        1. Title: “🔥 {query.upper()} X Sentiment 🔥”
        
        2. Total tweets analyzed: “📊 Total tweets: [count]”
        3. Sentiment breakdown:  
            ✅ Positive: [count] (avg score: [score])  
            ❌ Negative: [count] (avg score: [score])  
            ⚪ Neutral: [count]
        4. Dominant sentiment: “🏆 Dominant sentiment: [positive/neutral/negative]”

        5. **Momentum analysis:**
            - Write 1-2 lines indicating whether sentiment is **building up**, **flat**, or **cooling down**, based on the tweet content and engagement (likes/retweets/trending words).

        6. **Key emerging narratives:**
            List **3-5 bullet points** summarizing the trending topics (e.g., ETF inflow, memecoin surge, regulatory news, big influencer tweet).

        7. **Notable influencer activity:**
            Mention if any **influencer account (high retweet count and favorites)** is posting or boosting sentiment.

        8. **Top tweets:**
            List 1-2 highest engagement tweets in this format:
            - “@username: “[tweet text]” (RT: [retweets], ❤️: [likes])”

        👉 Format should be clear, readable, and friendly for crypto trader audience.

        Only output the report text, no extra explanation.

        Tweets:
        {data_to_analyze}
        """
        response = model.generate_content(prompt)

        # Check if response has text attribute
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            print(f"Unexpected response format from Gemini API: {response}")
            return "Failed to get a valid response from AI, try again later..."

    except Exception as e:
        print(f"Error occurred while fetching Gemini API: {e}")
        return "Failed while processing AI response, try again later..."

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
        list_tweet = await tweets(search_query=search_query, search_product="Top", minimum_tweets=30)
        
        if list_tweet and len(list_tweet) > 0:
            gemini_res = get_gemini_response(list_tweet, search_query)
            print(gemini_res)
        else:
            print("No tweets found or error occurred. Please try again later.")
        
        # Ask if user wants to continue
        continue_search = input("\nDo you want to search again? (y/n): ")
        if continue_search.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == '__main__':
    asyncio.run(main())
