from datetime import datetime
import google.generativeai as genai
from gemini.prompt import GEMINI_PROMPT
from config import GEMINI_API_KEY, GEMINI_MODEL, logger

# TODO* FETCH GEMINI API
def get_gemini_response(prompt):
    """
    Get response from Gemini API

    Args:
        prompt (str): Prompt to send to Gemini API
    Returns:
        str: Response from Gemini API or error message
    """
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # gemini-2.5-flash-preview-04-17
        # gemini-2.0-flash
        gemini_model = GEMINI_MODEL
    
        model = genai.GenerativeModel(gemini_model)
        response = model.generate_content(prompt)

        # Check if response has text attribute
        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            logger.error(f"Unexpected response format from Gemini API: {response}")
            return "Failed to get a valid response from AI, try again later..."

    except Exception as e:
        logger.error(f"Error occurred while fetching Gemini API: {e}")
        return "Failed while processing AI response, try again later..."
    

# TODO* ANALYZE WITH GEMINI
def gemini_analyze(tweets, query: str):
    
    print(f'{datetime.now()} - Analyzing all tweets, please wait...')
        
    prompt = GEMINI_PROMPT.format(
        search_query = query.upper(),
        tweets_to_analyze = tweets
    )
        
    analyze_result = get_gemini_response(prompt)
    return analyze_result
