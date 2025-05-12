import asyncio
from config import setup_logging
from gemini import gemini_analyze
from tweet import search_tweets, SentimentHistory
from visualization.chart import plot_sentiment_pie, plot_sentiment_trend, plot_sentiment_comparison
import os
from datetime import datetime

# Setup Logging for first time run
setup_logging()

# Create directory for charts if it doesn't exist
os.makedirs("charts", exist_ok=True)

# TODO* MAIN
async def main():
    # Initialize sentiment history
    sentiment_history = SentimentHistory()
    
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
            
            # Parse and save sentiment data
            sentiment_data = {
                "raw_result": analyze_result,
                "tweet_count": len(list_of_tweets)
            }
            
            sentiment_history.save_sentiment(search_query, sentiment_data)
            
            # Show historical comparison if available
            history = sentiment_history.get_sentiment_history(search_query)
            if len(history) > 1:
                print("\n📈 Historical Sentiment Trend:")
                for i, entry in enumerate(history[-3:], 1):
                    print(f"  {i}. {entry['timestamp']}: {entry['data']['raw_result'][:50]}...")
                
                # Ask if user wants to see charts
                show_charts = input("\nDo you want to show sentiment charts? (y/n): ")
                if show_charts.lower() == 'y':
                    # Generate and save charts
                    chart_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    
                    # Pie chart of current sentiment
                    pie_path = f"charts/{search_query.replace('#', '')}_pie_{chart_timestamp}.png"
                    plot_sentiment_pie(analyze_result, save_path=pie_path)
                    print(f"Pie chart saved to {pie_path}")
                    
                    # Line chart of sentiment trend
                    trend_path = f"charts/{search_query.replace('#', '')}_trend_{chart_timestamp}.png"
                    plot_sentiment_trend(history, search_query, save_path=trend_path)
                    print(f"Trend chart saved to {trend_path}")
                    
                    # Stacked area chart
                    if len(history) >= 2:
                        stack_path = f"charts/{search_query.replace('#', '')}_stack_{chart_timestamp}.png"
                        plot_sentiment_comparison(history, search_query, save_path=stack_path)
                        print(f"Stacked area chart saved to {stack_path}")
            
            print(analyze_result)  # Print the analyze_result
        else:
            print("No tweets found for the given query.")
        
        # Ask if user wants to continue
        continue_search = input("\nDo you want to search again? (y/n): ")
        if continue_search.lower() != 'y':
            print("Exiting program. Goodbye!")
            break


if __name__ == '__main__':
    asyncio.run(main())
