import json
import os
from datetime import datetime

class SentimentHistory:
    def __init__(self, history_file="sentiment_history.json"):
        self.history_file = history_file
        self.history = self._load_history()
    
    def _load_history(self):
        """Load sentiment history from file"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_sentiment(self, query, sentiment_data):
        """Save sentiment data with timestamp"""
        timestamp = datetime.now().isoformat()
        
        if query not in self.history:
            self.history[query] = []
            
        # Add new sentiment data with timestamp
        entry = {
            "timestamp": timestamp,
            "data": sentiment_data
        } 
        
        self.history[query].append(entry)
        
        # Save to file
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def get_sentiment_history(self, query, limit=5):
        """Get historical sentiment data for a query"""
        if query in self.history:
            return self.history[query][-limit:]
        return []