# Article Sentiment Analyzer

## Overview
This project is a Streamlit-based web application that analyzes the sentiment of an article from a given URL. It uses web scraping techniques with Selenium and BeautifulSoup to extract text from the webpage and applies natural language processing (NLP) techniques to determine the sentiment (Positive, Negative, or Neutral).

## Features
- Extracts and processes text from a given URL.
- Cleans and tokenizes text data.
- Identifies and counts positive and negative words.
- Calculates the polarity score to determine sentiment.
- Provides an interactive chatbot-style user interface with Streamlit.

## Technologies Used
- Python
- Streamlit (for UI)
- Selenium (for web scraping dynamic content)
- BeautifulSoup (for HTML parsing)
- NLTK (for text processing and sentiment analysis)
- WebDriver Manager (for Selenium)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/article-sentiment-analyzer.git
   cd article-sentiment-analyzer
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:

## Setup
Make sure you have the required WebDriver installed for Selenium. The script automatically installs ChromeDriver using `webdriver-manager`.

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Enter the URL of an article in the input box.
3. The application will extract the content, analyze its sentiment, and display the results.

## Output
- Extracted title and content summary.
- Positive, negative, and polarity scores.
- Final sentiment classification (Positive, Negative, Neutral).

## Future Improvements
- Improve handling of dynamically loaded content.
- Expand the dictionary for sentiment analysis.
- Add more advanced NLP techniques like sentiment classification using machine learning.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
https://github.com/sachinchoudharyy

