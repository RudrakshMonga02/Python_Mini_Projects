# Text Analyzer

A Python application that analyzes text files to provide comprehensive statistics and insights about the content.

## Features

- **Word Count**: Counts total number of words in the text
- **Character Count**: Counts characters with and without spaces
- **Sentence Count**: Counts the number of sentences in the text
- **Word Frequency Analysis**: Identifies the 10 most common words (excluding stop words)
- **Statistical Insights**: Calculates average word length and words per sentence

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

## Installation

Simply download or clone the repository. No additional dependencies need to be installed.

## Usage

### Running the Program

```bash
python main.py
```

### Example

```
$ python main.py
============================================================
WELCOME TO TEXT ANALYZER
============================================================
Enter the path to the text file to analyze: sample.txt

Reading file...
============================================================
TEXT ANALYZER RESULTS
============================================================
File analyzed: sample.txt
------------------------------------------------------------

BASIC STATISTICS:
  • Total words: 1250
  • Total characters (with spaces): 7500
  • Total characters (without spaces): 6150
  • Total sentences: 45
  • Average word length: 4.92 characters
  • Average words per sentence: 27.78

TOP 10 MOST FREQUENT WORDS (excluding common words):
  1. 'python' - 45 times (3.6%)
  2. 'code' - 38 times (3.0%)
  ...

============================================================

Would you like to analyze another file? (yes/no): no
Thank you for using Text Analyzer!
```

## File Structure

- `main.py` - Main application file containing all analysis functions
- `README.md` - This file with usage documentation
- `LEARNING_GUIDE.md` - Educational guide explaining the concepts and implementation

## Function Reference

### Core Functions

#### `read_file(filename)`
Reads and returns the contents of a text file.
- **Input**: filename (str)
- **Output**: File contents (str) or empty string if error

#### `count_words(text)`
Counts the total number of words.
- **Input**: text (str)
- **Output**: Word count (int)

#### `count_characters(text)`
Counts characters with and without spaces.
- **Input**: text (str)
- **Output**: Dictionary with 'with_spaces' and 'without_spaces' counts

#### `count_sentences(text)`
Counts the number of sentences using regex.
- **Input**: text (str)
- **Output**: Sentence count (int)

#### `most_common_words(text, top_n=10)`
Finds the most frequently occurring words using Counter.
- **Input**: text (str), top_n (int, default=10)
- **Output**: List of tuples (word, frequency)

#### `display_results(filename, text)`
Displays all analysis results in a formatted output.
- **Input**: filename (str), text (str)
- **Output**: Formatted results printed to console

### Main Program Flow

The `main()` function orchestrates the entire workflow:
1. Prompts user for filename
2. Checks if file exists
3. Reads file content
4. Calls display_results to show analysis
5. Offers option to analyze another file

## Error Handling

The program includes error handling for:
- File not found
- File read errors
- Invalid user input
- Empty file content

## Learning Outcomes

This project demonstrates:
- **File I/O**: Reading files with proper error handling
- **String Manipulation**: Using split(), regex, and string methods
- **Dictionaries & Counters**: Using Counter for frequency analysis
- **Data Structure**: Working with lists, tuples, and dictionaries
- **Control Flow**: Loops, conditionals, and user input
- **Functions**: Modular design with clear responsibilities
- **Formatting**: Professional output presentation

## Tips for Enhancement

Consider adding:
- Command-line arguments for filename and top words count
- Export results to JSON or CSV
- Comparison between multiple files
- Syllable counting
- Readability score calculation
- Custom stop word lists
- Filter common/uncommon words dynamically

## License

Free to use and modify for educational purposes.
