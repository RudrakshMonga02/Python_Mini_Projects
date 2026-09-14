# Text Analyzer - Learning Guide

This guide explains the key concepts and implementation details of the Text Analyzer project.

## Learning Focus Areas

### 1. File Reading (File I/O)

#### Concept
File reading is the process of opening a file and reading its contents into memory. In Python, we use the `open()` function.

#### Implementation in `read_file()`

```python
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
```

#### Key Points
- **`open(filename, 'r', encoding='utf-8')`**: Opens file in read mode ('r') with UTF-8 encoding
- **`with` statement**: Context manager that automatically closes the file
- **Try-except**: Error handling for file not found and other I/O errors
- **`file.read()`**: Reads entire file content as a string

#### Why Context Manager?
```python
# Good - automatically closes file
with open(filename, 'r') as file:
    content = file.read()

# Bad - file may not close if error occurs
file = open(filename, 'r')
content = file.read()
file.close()
```

---

### 2. String Manipulation

#### Concept
String manipulation involves processing and transforming text data. Python provides many built-in string methods.

#### Key String Methods Used

**a) `.split()` - Split string into words**
```python
text = "Hello world Python is awesome"
words = text.split()
# Result: ['Hello', 'world', 'Python', 'is', 'awesome']

word_count = len(words)  # Result: 5
```

**b) `.lower()` - Convert to lowercase**
```python
text = "Hello World"
text_lower = text.lower()
# Result: "hello world"
```

**c) `.replace()` - Replace characters**
```python
text = "Hello world"
text_no_spaces = text.replace(" ", "")
# Result: "Helloworld"
```

**d) `.strip()` - Remove whitespace**
```python
text = "  hello  "
text_clean = text.strip()
# Result: "hello"
```

**e) Regular Expressions with `re` module**
```python
import re

# Find sentences using regex
text = "Hello. World! How are you?"
sentences = re.split(r'[.!?]+', text)

# Find all words (letters only)
words = re.findall(r'\b[a-z]+\b', text.lower())
```

---

### 3. Dictionaries

#### Concept
Dictionaries store data as key-value pairs. They're perfect for counting frequencies.

#### Dictionary Basics

```python
# Create a dictionary
word_freq = {}

# Add items
word_freq['python'] = 5
word_freq['code'] = 3
word_freq['data'] = 4

# Access items
print(word_freq['python'])  # Output: 5

# Update items
word_freq['python'] += 1    # Now 6

# Check if key exists
if 'python' in word_freq:
    print("Found!")

# Iterate through dictionary
for word, frequency in word_freq.items():
    print(f"{word}: {frequency}")
```

#### Manual Word Frequency Count
```python
def count_word_frequency_manual(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Usage
text = "apple banana apple cherry banana apple"
words = text.split()
freq = count_word_frequency_manual(words)
# Result: {'apple': 3, 'banana': 2, 'cherry': 1}
```

#### Using `Counter` (More Efficient)
The `collections.Counter` class simplifies frequency counting:

```python
from collections import Counter

text = "apple banana apple cherry banana apple"
words = text.split()

word_freq = Counter(words)
print(word_freq)                    # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(word_freq.most_common(2))     # [('apple', 3), ('banana', 2)]
```

#### Dictionary Comprehension
```python
# Create dictionary of word lengths
words = ['python', 'code', 'data']
word_lengths = {word: len(word) for word in words}
# Result: {'python': 6, 'code': 4, 'data': 4}
```

---

## How It All Works Together

### Function-by-Function Breakdown

#### 1. `read_file(filename)`
**Purpose**: Load text from disk into memory
**Learning**: File I/O with error handling
```
Input: "example.txt"
↓
Opens file, reads content
↓
Output: "The text content..."
```

#### 2. `count_words(text)`
**Purpose**: Count total words
**Learning**: String manipulation with `.split()`
```
Input: "Hello world" 
↓
Split on whitespace
↓
Output: 2
```

#### 3. `count_characters(text)`
**Purpose**: Count chars with/without spaces
**Learning**: String methods (`.replace()`, `len()`)
```
Input: "Hello world"
↓
Len with spaces: 11
Len without spaces: 10
↓
Output: {'with_spaces': 11, 'without_spaces': 10}
```

#### 4. `count_sentences(text)`
**Purpose**: Count sentence endpoints
**Learning**: Regular expressions with `re.split()`
```
Input: "Hello. World! How are you?"
↓
Split on .!?
↓
Output: 3
```

#### 5. `most_common_words(text, top_n=10)`
**Purpose**: Find frequently occurring words
**Learning**: Dictionaries + Counter + filtering
```
Input: text, top_n=10
↓
1. Convert to lowercase
2. Extract words with regex
3. Filter stop words (common words)
4. Count frequencies with Counter
5. Get top N words
↓
Output: [('python', 45), ('code', 38), ...]
```

#### 6. `display_results(filename, text)`
**Purpose**: Present all analysis results
**Learning**: Formatting, f-strings, data presentation
```
Input: filename, text
↓
Call functions 1-5
↓
Format and print results
↓
Output: Beautiful formatted report
```

---

## Advanced Concepts

### Stop Words
Stop words are common words that don't add much meaning. By filtering them out, we get more meaningful results:

```python
stop_words = {'the', 'a', 'an', 'and', 'is', 'was', ...}

# Without filtering
Counter(['the', 'the', 'the', 'python', 'code'])
# Most common: 'the'

# With filtering
Counter(['python', 'code'])
# Most common: 'python' or 'code'
```

### Regular Expressions
Regular expressions (regex) find patterns in text:

```python
import re

# Pattern: \b[a-z]+\b
# \b = word boundary
# [a-z]+ = one or more lowercase letters
# Example: matches 'hello' in "Hello! 123world"

text = "Hello123 world!"
words = re.findall(r'\b[a-z]+\b', text.lower())
# Result: ['hello', 'world']
```

### Exception Handling
Handle errors gracefully:

```python
try:
    # Try to load file
    content = read_file(filename)
except FileNotFoundError:
    # File doesn't exist
    print("File not found")
except Exception as e:
    # Other errors
    print(f"Error: {e}")
```

---

## Practice Exercises

### Exercise 1: Manual Dictionary Count
Create a function that counts word frequency without using Counter:

```python
def count_frequencies(text):
    words = text.split()
    freq = {}
    for word in words:
        # Add to frequency count
        pass
    return freq
```

### Exercise 2: Custom Stop Words
Modify `most_common_words()` to accept a list of custom stop words:

```python
def most_common_words(text, stop_words=None, top_n=10):
    # Use custom stop words if provided
    # Otherwise use default
    pass
```

### Exercise 3: Statistics Enhancement
Add these statistics:
- Longest word
- Shortest word (excluding 1-letter words)
- Average sentence length
- Unique words count

```python
def calculate_advanced_stats(text):
    # Calculate and return advanced statistics
    pass
```

### Exercise 4: File Comparison
Compare statistics between two files:

```python
def compare_files(file1, file2):
    # Read both files
    # Calculate statistics for each
    # Display comparison
    pass
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Not Handling File Errors
```python
# Bad
with open(filename) as file:
    content = file.read()

# Good
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

### ❌ Mistake 2: Including Stop Words in Frequency
```python
# Bad - includes common words
words = text.lower().split()
freq = Counter(words)  # 'the' will dominate!

# Good - filter first
stop_words = {'the', 'a', 'an', ...}
words = [w for w in text.lower().split() if w not in stop_words]
freq = Counter(words)
```

### ❌ Mistake 3: Case-Sensitive Comparison
```python
# Bad - treats "Python" and "python" differently
words = text.split()
freq = Counter(words)

# Good - normalize case first
words = text.lower().split()
freq = Counter(words)
```

### ❌ Mistake 4: Including Punctuation
```python
# Bad - "world," and "world" are different
words = text.lower().split()

# Good - remove punctuation first
words = re.findall(r'\b[a-z]+\b', text.lower())
```

---

## Key Takeaways

1. **File I/O**: Use context managers (`with` statement) for safe file handling
2. **String Methods**: `.split()`, `.lower()`, `.replace()` are fundamental
3. **Dictionaries**: Perfect for counting and mapping data
4. **Counter Class**: Makes frequency analysis simple and efficient
5. **Regular Expressions**: Powerful for pattern matching in text
6. **Error Handling**: Always anticipate and handle potential errors
7. **Data Filtering**: Stop word filtering improves result quality
8. **Code Organization**: Modular functions are reusable and testable

---

## Additional Resources

- Python `re` module: https://docs.python.org/3/library/re.html
- Python `collections`: https://docs.python.org/3/library/collections.html
- String methods: https://docs.python.org/3/library/stdtypes.html#string-methods
- File I/O: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

Happy Learning! 🎓
