# Learning Guide: API Data Fetcher 📚

This guide explains the key concepts and learning objectives covered in this project.

## What You'll Learn

This project covers four main learning areas:

1. **APIs & HTTP Requests**
2. **JSON Parsing & Data Handling**
3. **Error Handling & Exceptions**
4. **Building Interactive CLI Applications**

---

## 1. APIs & HTTP Requests 🌐

### What is an API?

An **API (Application Programming Interface)** is a bridge between applications that allows them to communicate and share data.

**Real-World Analogy:** Think of an API like a restaurant menu:
- You (the client) request a dish
- The menu (the API) tells you what's available
- The chef (the server) prepares and returns your order

### HTTP Methods

The most common HTTP methods are:

| Method | Purpose | Example |
|--------|---------|---------|
| **GET** | Retrieve data | `requests.get(url)` |
| **POST** | Send/create data | Submit a form |
| **PUT** | Update data | Modify a resource |
| **DELETE** | Remove data | Delete a record |

In this project, we use **GET** to fetch data:

```python
response = requests.get(api_url, timeout=5)
```

### The `requests` Library

The `requests` library makes HTTP calls simple:

```python
import requests

# Make a GET request
response = requests.get('https://api.example.com/data')

# Get the response status code (200 = success)
print(response.status_code)

# Get the response data
data = response.json()  # Parse JSON response
```

**Key Methods:**
- `response.json()` - Parse JSON response body
- `response.text` - Get response as text
- `response.status_code` - Check if request succeeded (200 = OK)

### Status Codes

| Code | Meaning | Common Reason |
|------|---------|---------------|
| **200** | OK | Request successful ✅ |
| **400** | Bad Request | Invalid parameters |
| **401** | Unauthorized | API key required |
| **404** | Not Found | Endpoint doesn't exist |
| **500** | Server Error | API server problem |

---

## 2. JSON Parsing & Data Handling 📊

### What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight format for storing and exchanging data.

**JSON Structure:**
```json
{
  "type": "single",
  "joke": "Why do programmers prefer dark mode?",
  "category": "Programming"
}
```

### Parsing JSON in Python

When you fetch data from an API, it comes as JSON text. Python needs to convert it to a dictionary:

```python
import requests
import json

# Fetch data
response = requests.get('https://v2.jokeapi.dev/joke/Any')

# Method 1: Using .json() method (preferred)
data = response.json()
print(data['joke'])  # Access like a dictionary

# Method 2: Using json.loads()
data = json.loads(response.text)
```

### Accessing Nested Data

JSON can have nested structures:

```python
# JSON structure:
# {
#   "user": {
#     "name": "John",
#     "location": {
#       "city": "New York"
#     }
#   }
# }

data = response.json()

# Access nested values
print(data['user']['name'])           # "John"
print(data['user']['location']['city'])  # "New York"

# Safe access with .get() to avoid KeyError
print(data.get('user', {}).get('name', 'Unknown'))
```

### Pretty-Printing JSON

The `json.dumps()` function formats JSON nicely:

```python
import json

data = {'name': 'Alice', 'age': 30}

# Pretty print with 2-space indentation
print(json.dumps(data, indent=2))

# Output:
# {
#   "name": "Alice",
#   "age": 30
# }
```

---

## 3. Error Handling & Exceptions 🛡️

### Why Handle Errors?

When fetching from APIs, things can go wrong:
- No internet connection
- API server is down
- Invalid URL
- Timeout waiting for response

**Bad approach:** Program crashes without explanation  
**Good approach:** Catch errors and provide helpful messages

### The Try-Except Block

```python
try:
    # Code that might cause an error
    response = requests.get(api_url)
    data = response.json()
except requests.exceptions.RequestException as e:
    # Handle the error gracefully
    print("Failed to fetch data:", e)
```

### Types of Errors in API Fetching

```python
import requests

try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()  # Raise error for bad status codes
    data = response.json()
    
except requests.exceptions.Timeout:
    print("Request timed out - server took too long to respond")
    
except requests.exceptions.ConnectionError:
    print("Network error - check your internet connection")
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")  # 404, 500, etc.
    
except json.JSONDecodeError:
    print("Invalid JSON response")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

### In Our Project

The `handle_errors()` function checks if fetching failed:

```python
def handle_errors(response_data):
    if response_data is None:
        print("❌ Error: Failed to fetch data from API")
        return True
    return False
```

---

## 4. Building Interactive CLI Applications 💻

### What is a CLI?

A **CLI (Command-Line Interface)** is a program you interact with by typing commands in a terminal.

**Examples:**
- `ls` or `dir` - list files
- `git commit` - version control
- Our API Data Fetcher - interactive menu

### CLI Design Patterns

#### Menu Loop

The core of an interactive CLI is an infinite loop:

```python
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")
    
    choice = input("Select: ").strip()
    
    if choice == "3":
        break  # Exit the loop
    
    # Handle choices...
```

#### Input Validation

Always validate user input:

```python
choice = input("Select (1-3): ").strip()

if choice not in ["1", "2", "3"]:
    print("Invalid choice!")
    continue  # Ask again
```

#### User-Friendly Messages

Make the CLI friendly with emojis and formatting:

```python
print("🔗 Welcome to API Data Fetcher!")          # Welcoming
print("=" * 60)                                   # Visual separator
print("⏳ Fetching data...")                      # Status indicator
print("❌ Error: Failed to fetch data")           # Error message
print("✅ Success!")                              # Success message
```

### In Our Project

The `main()` function implements a complete CLI:

```python
def main():
    while True:
        # Display menu
        print("\nAvailable APIs:")
        print("  1. Random Joke")
        print("  2. Random User")
        
        # Get input
        choice = input("\nSelect an API (1-3): ").strip()
        
        # Validate
        if choice not in ["1", "2", "3"]:
            print("Invalid choice")
            continue
        
        # Process
        if choice == "3":
            break
        
        # ... fetch and display data
```

---

## Code Flow Diagram

```
main()
  ↓
Display Menu
  ↓
Get User Choice
  ↓
Fetch Data with fetch_data()
  ↓
Check Errors with handle_errors()
  ↓
Display With display_data()
  ↓
Ask to Repeat?
  ├─ Yes → Back to "Get User Choice"
  └─ No → Exit
```

---

## Key Functions Explained

### `fetch_data(api_url)`

```python
def fetch_data(api_url: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(api_url, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as e:
        return None
```

**What it does:**
1. Makes HTTP GET request to the URL
2. Parses JSON response
3. Returns data on success, `None` on failure
4. Timeout prevents hanging forever

**Learning points:**
- Type hints (`-> Optional[Dict]`)
- Exception handling
- Using external library (`requests`)

### `display_data(data, api_type)`

```python
def display_data(data: Dict[str, Any], api_type: str = "general"):
    if api_type == "joke":
        print(f"Setup: {data.get('setup')}")
        print(f"Delivery: {data.get('delivery')}")
    else:
        print(json.dumps(data, indent=2))
```

**What it does:**
1. Checks the type of API
2. Formats data appropriately
3. Displays in readable format

**Learning points:**
- Dictionary access with `.get()`
- Conditional formatting
- Pretty-printing JSON

### `handle_errors(response_data, error_type)`

```python
def handle_errors(response_data, error_type: str = "api") -> bool:
    if response_data is None:
        print("❌ Error: Failed to fetch data")
        return True
    return False
```

**What it does:**
1. Checks if data is None (indicates error)
2. Prints helpful error message
3. Returns boolean indicating error status

**Learning points:**
- Error reporting
- Return values for flow control
- User-friendly messages

---

## Hands-On Exercises

### Exercise 1: Add a New API

Add a new API to the `apis` dictionary in `main()`:

```python
"5": {
    "name": "Dog Facts",
    "url": "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1",
    "type": "general"
}
```

### Exercise 2: Custom Formatting

Add custom formatting for the "Random User" API in `display_data()`:

```python
if api_type == "user":
    data = data.get('results', [{}])[0]
    print(f"Name: {data.get('name', {}).get('first')} {data.get('name', {}).get('last')}")
    print(f"Email: {data.get('email')}")
```

### Exercise 3: Save Results

Modify the code to save API responses to a file:

```python
import json
from datetime import datetime

# After fetching data:
with open(f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", "w") as f:
    json.dump(data, f, indent=2)
print("✅ Response saved!")
```

### Exercise 4: API Rate Limiting

Add a delay between requests to respect API rate limits:

```python
import time

# After displaying data:
time.sleep(1)  # Wait 1 second before next request
```

---

## Common Mistakes to Avoid

❌ **Mistake 1: Not handling errors**
```python
# Bad
response = requests.get(url)
data = response.json()  # Crashes if no internet

# Good
try:
    response = requests.get(url)
    data = response.json()
except requests.exceptions.RequestException:
    print("Error fetching data")
```

❌ **Mistake 2: Assuming API structure**
```python
# Bad
print(data['joke'])  # KeyError if key doesn't exist

# Good
print(data.get('joke', 'No joke available'))
```

❌ **Mistake 3: No timeout**
```python
# Bad
response = requests.get(url)  # Can hang forever

# Good
response = requests.get(url, timeout=5)  # Timeout after 5 seconds
```

❌ **Mistake 4: Ignoring status codes**
```python
# Bad
response = requests.get(url)
data = response.json()  # Works even if status is 404

# Good
if response.status_code != 200:
    print(f"Error: {response.status_code}")
```

---

## Resources

📚 **Official Documentation:**
- [Requests Library Docs](https://requests.readthedocs.io/)
- [Python json module](https://docs.python.org/3/library/json.html)
- [HTTP Status Codes](https://httpstatuses.com/)

🎓 **Learning Resources:**
- [REST API Basics](https://restfulapi.net/)
- [JSON Tutorial](https://www.json.org/)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)

🔗 **Free APIs to Try:**
- [Public APIs List](https://github.com/public-apis/public-apis)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - Fake API for testing
- [OpenWeatherMap](https://openweathermap.org/api) - Weather data

---

## Summary

After completing this project, you understand:

✅ How APIs work and how to use them  
✅ How to parse JSON data in Python  
✅ How to handle errors gracefully  
✅ How to build interactive CLI applications  
✅ Best practices for API integration  
✅ Type hints and clean code practices  

**Next Steps:** Try modifying the project, add new features, or integrate a different API!
