import streamlit as st
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import time

# Load positive and negative words
with open('MasterDictionary/positive-words.txt', 'r') as f:
    positive_words = set(f.read().split())

with open('MasterDictionary/negative-words.txt', 'r') as f:
    negative_words = set(f.read().split())

# Set of stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Cleans the text by removing punctuation, converting to lowercase, and removing stopwords."""
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return words

def positive_score(words):
    """Counts how many positive words are in the text."""
    return sum(1 for word in words if word in positive_words)

def negative_score(words):
    """Counts how many negative words are in the text."""
    return sum(1 for word in words if word in negative_words)

def polarity_score(pos_score, neg_score):
    """Calculates the polarity score based on positive and negative word counts."""
    return (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)

def analyze_sentiment(url):
    """Extracts the content of the URL and returns its sentiment (positive/negative)."""
    try:
        # Set up Selenium WebDriver (Chrome in this case)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        # Wait for content to load (adjust as needed for dynamic content)
        time.sleep(3)  # Wait for JavaScript to load the content

        # Use BeautifulSoup to parse the page content
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Get title, paragraphs, and additional headings
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No title found"
        paragraphs = soup.find_all('p')
        additional_headings = soup.find_all(['h2', 'h3', 'h4'])

        # Combine content from paragraphs and headings
        article_text = '\n'.join([p.get_text(strip=True) for p in paragraphs])
        article_text += '\n'.join([heading.get_text(strip=True) for heading in additional_headings])

        # Clean and analyze the content
        words = clean_text(article_text)
        pos_score = positive_score(words)
        neg_score = negative_score(words)
        
        # Get polarity score and determine sentiment
        polarity = polarity_score(pos_score, neg_score)
        
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        driver.quit()  # Close the browser

        return title, article_text, sentiment

    except Exception as e:
        return None, None, f"Error: {e}"

# Streamlit chatbot-like interface
st.title("Article Sentiment Analyzer Chatbot")

# Simulate chatbot interaction
st.write("👋 Hello! I'm here to help you analyze the sentiment of an article. Please provide the URL of the article you'd like to analyze.")

# Input URL
url = st.text_input("Enter the URL of the article:")

if url:
    st.write("🔍 Analyzing the article... Please wait.")

    # Get the title, content, and sentiment of the article
    title, article_text, sentiment = analyze_sentiment(url)
    
    if title:
        st.write(f"### Title: {title}")
        st.write(f"#### Content (first 500 characters):")
        st.write(article_text[:500])  # Show first 500 characters of the article
        st.write(f"#### Sentiment: {sentiment}")
    else:
        st.write("❌ Could not extract or analyze content. Please check the URL and try again.")
