import matplotlib.pyplot as plt
import re
from datetime import datetime

def extract_sentiment_scores(raw_result):
    """Extract sentiment scores from raw result text"""
    positive_match = re.search(r'Positive: (\d+) \(avg score: ([\d.-]+)\)', raw_result)
    negative_match = re.search(r'Negative: (\d+) \(avg score: ([\d.-]+)\)', raw_result)
    neutral_match = re.search(r'Neutral: (\d+)', raw_result)
    
    positive = int(positive_match.group(1)) if positive_match else 0
    negative = int(negative_match.group(1)) if negative_match else 0
    neutral = int(neutral_match.group(1)) if neutral_match else 0
    
    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }

def plot_sentiment_pie(raw_result, save_path=None):
    """Create a pie chart of sentiment distribution"""
    scores = extract_sentiment_scores(raw_result)
    
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [scores['positive'], scores['negative'], scores['neutral']]
    colors = ['#4CAF50', '#F44336', '#9E9E9E']
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'Sentiment Distribution - {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    
    # if save_path:
    #     plt.savefig(save_path)
    #     return save_path
    # else:
    #     plt.show()
    #     return None
    if save_path:
        plt.savefig(save_path)
        plt.show()
        return save_path
    
def plot_sentiment_trend(sentiment_history, query, save_path=None):
    """Create a line chart showing sentiment trend over time"""
    if not sentiment_history:
        return None
    
    # Extract timestamps and sentiment scores
    timestamps = []
    positive_scores = []
    negative_scores = []
    neutral_scores = []
    
    for entry in sentiment_history:
        # Convert ISO timestamp to datetime for better display
        timestamp = datetime.fromisoformat(entry['timestamp'])
        timestamps.append(timestamp)
        
        # Extract sentiment scores
        raw_result = entry['data']['raw_result']
        scores = extract_sentiment_scores(raw_result)
        
        positive_scores.append(scores['positive'])
        negative_scores.append(scores['negative'])
        neutral_scores.append(scores['neutral'])
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot each sentiment type
    plt.plot(timestamps, positive_scores, 'g-', marker='o', label='Positive')
    plt.plot(timestamps, negative_scores, 'r-', marker='o', label='Negative')
    plt.plot(timestamps, neutral_scores, 'b-', marker='o', label='Neutral')
    
    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Number of Tweets')
    plt.title(f'Sentiment Trend for {query}')
    plt.legend()
    
    # Format x-axis to show readable dates
    plt.gcf().autofmt_xdate()
    
    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # if save_path:
    #     plt.savefig(save_path)
    #     return save_path
    # else:
    #     plt.show()
    #     return None
    if save_path:
        plt.savefig(save_path)
        plt.show()
        return save_path

def plot_sentiment_comparison(sentiment_history, query, save_path=None):
    """Create a stacked area chart showing sentiment composition over time"""
    if not sentiment_history or len(sentiment_history) < 2:
        return None
    
    # Extract timestamps and sentiment scores
    timestamps = []
    positive_scores = []
    negative_scores = []
    neutral_scores = []
    
    for entry in sentiment_history:
        # Convert ISO timestamp to datetime for better display
        timestamp = datetime.fromisoformat(entry['timestamp'])
        timestamps.append(timestamp)
        
        # Extract sentiment scores
        raw_result = entry['data']['raw_result']
        scores = extract_sentiment_scores(raw_result)
        
        positive_scores.append(scores['positive'])
        negative_scores.append(scores['negative'])
        neutral_scores.append(scores['neutral'])
    
    # Create the stacked area plot
    plt.figure(figsize=(10, 6))
    
    # Create the stacked plot
    plt.stackplot(timestamps, 
                 positive_scores, 
                 neutral_scores,
                 negative_scores,
                 labels=['Positive', 'Neutral', 'Negative'],
                 colors=['#4CAF50', '#9E9E9E', '#F44336'],
                 alpha=0.8)
    
    # Add labels and title
    plt.xlabel('Time')
    plt.ylabel('Number of Tweets')
    plt.title(f'Sentiment Composition for {query} Over Time')
    plt.legend(loc='upper left')
    
    # Format x-axis to show readable dates
    plt.gcf().autofmt_xdate()
    
    # Add grid for better readability
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # if save_path:
    #     plt.savefig(save_path)
    #     return save_path
    # else:
    #     plt.show()
    #     return None
    if save_path:
        plt.savefig(save_path)
        plt.show()
        return save_path

