"""
Text Analyzer - Analyzes text files for various metrics
Features: Word count, character count, sentence count, and word frequency analysis
"""

import os
from collections import Counter
import re


def read_file(filename):
    """
    Read and return the contents of a text file.
    
    Args:
        filename (str): Path to the text file
        
    Returns:
        str: Contents of the file, or empty string if file doesn't exist
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def count_words(text):
    """
    Count the total number of words in the text.
    
    Args:
        text (str): Input text
        
    Returns:
        int: Total number of words
    """
    # Split text into words and filter out empty strings
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Count total characters and characters without spaces.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Dictionary with 'with_spaces' and 'without_spaces' counts
    """
    total_with_spaces = len(text)
    total_without_spaces = len(text.replace(" ", ""))
    
    return {
        'with_spaces': total_with_spaces,
        'without_spaces': total_without_spaces
    }


def count_sentences(text):
    """
    Count the number of sentences in the text.
    Sentences end with '.', '!', or '?'
    
    Args:
        text (str): Input text
        
    Returns:
        int: Number of sentences
    """
    # Use regex to find sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)


def most_common_words(text, top_n=10):
    """
    Find the most frequently occurring words in the text.
    Uses dictionary-based frequency analysis.
    
    Args:
        text (str): Input text
        top_n (int): Number of top words to return (default: 10)
        
    Returns:
        list: List of tuples (word, frequency) sorted by frequency
    """
    # Convert to lowercase and remove punctuation
    text_lower = text.lower()
    # Remove punctuation and split into words
    words = re.findall(r'\b[a-z]+\b', text_lower)
    
    # Common English stop words to filter out
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'is', 'are', 'was', 'were', 'be',
        'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
        'would', 'could', 'should', 'may', 'might', 'must', 'can', 'i', 'you',
        'he', 'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where',
        'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most',
        'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'same', 'so',
        'than', 'too', 'very', 'just', 'as', 'if'
    }
    
    # Filter out stop words
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Use Counter to count word frequencies
    word_freq = Counter(filtered_words)
    
    # Return top N most common words
    return word_freq.most_common(top_n)


def display_results(filename, text):
    """
    Display all analysis results for the text file.
    
    Args:
        filename (str): Name of the analyzed file
        text (str): The text content that was analyzed
    """
    if not text:
        print("No text to analyze.")
        return
    
    # Calculate all metrics
    word_count = count_words(text)
    char_count = count_characters(text)
    sentence_count = count_sentences(text)
    common_words = most_common_words(text, top_n=10)
    
    # Display results
    print("\n" + "="*60)
    print(f"TEXT ANALYZER RESULTS")
    print("="*60)
    print(f"File analyzed: {filename}")
    print("-"*60)
    
    print(f"\nBASIC STATISTICS:")
    print(f"  • Total words: {word_count}")
    print(f"  • Total characters (with spaces): {char_count['with_spaces']}")
    print(f"  • Total characters (without spaces): {char_count['without_spaces']}")
    print(f"  • Total sentences: {sentence_count}")
    
    if word_count > 0:
        avg_word_length = char_count['without_spaces'] / word_count
        avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
        print(f"  • Average word length: {avg_word_length:.2f} characters")
        print(f"  • Average words per sentence: {avg_words_per_sentence:.2f}")
    
    print(f"\nTOP 10 MOST FREQUENT WORDS (excluding common words):")
    if common_words:
        for rank, (word, frequency) in enumerate(common_words, 1):
            percentage = (frequency / word_count) * 100 if word_count > 0 else 0
            print(f"  {rank:2d}. '{word}' - {frequency} times ({percentage:.1f}%)")
    else:
        print("  No words found to analyze.")
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function to run the text analyzer."""
    print("="*60)
    print("WELCOME TO TEXT ANALYZER")
    print("="*60)
    
    # Get filename from user
    filename = input("Enter the path to the text file to analyze: ").strip()
    
    # Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        return
    
    # Read the file
    print("\nReading file...")
    text = read_file(filename)
    
    # Display results
    display_results(filename, text)
    
    # Offer additional analysis
    while True:
        choice = input("Would you like to analyze another file? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            main()
            break
        elif choice in ['no', 'n']:
            print("Thank you for using Text Analyzer!")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
