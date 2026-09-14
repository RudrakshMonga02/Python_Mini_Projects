# API Data Fetcher 🔗

A Python CLI tool that demonstrates how to fetch and process data from public APIs with proper error handling.

## Features

✅ **Fetch Data from Public APIs** - Send HTTP requests to API endpoints and retrieve data  
✅ **JSON Parsing** - Automatically parse and handle JSON responses  
✅ **Error Handling** - Graceful error management for network and API failures  
✅ **Formatted Display** - Pretty-print API responses in an organized way  
✅ **Repeated Fetching** - Fetch multiple times without restarting the program  
✅ **Multiple APIs** - Pre-configured examples with custom URL support  

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download this project
2. Install the required library:
```bash
pip install requests
```

## Usage

Run the CLI application:
```bash
python main.py
```

### Interactive Menu

The program presents a friendly CLI menu:

```
🔗 Welcome to API Data Fetcher!
============================================================

Available APIs:
  1. Random Joke (JokeAPI)
  2. Random User
  3. Cat Facts
  4. Custom URL
  5. Exit

Select an API (1-5):
```

**Options:**
- **1-3**: Pre-configured public API endpoints (no API key required)
- **4**: Enter a custom API URL to fetch from any endpoint
- **5**: Exit the program

After fetching, the program asks if you want to fetch again or exit.

## Example APIs (Included)

| API | URL | Returns |
|-----|-----|---------|
| **Joke API** | `https://v2.jokeapi.dev/joke/Any` | Random jokes in JSON format |
| **Random User** | `https://randomuser.me/api/` | Random user profile data |
| **Cat Facts** | `https://catfact.ninja/random` | Random cat facts |

## Code Structure

### Functions

#### `fetch_data(api_url: str)`
- **Purpose**: Makes HTTP GET request to the API endpoint
- **Parameters**: `api_url` - The URL of the API to fetch from
- **Returns**: Parsed JSON response as dictionary, or `None` if request fails
- **Error Handling**: Uses try-except to catch network errors

#### `display_data(data: Dict[str, Any], api_type: str = "general")`
- **Purpose**: Formats and displays the API response in a readable way
- **Parameters**: 
  - `data` - The parsed JSON data from API
  - `api_type` - Type of API for custom formatting (default: "general")
- **Features**: Handles special formatting for joke API, generic JSON display

#### `handle_errors(response_data, error_type: str = "api")`
- **Purpose**: Checks for errors and provides helpful error messages
- **Parameters**:
  - `response_data` - The response from fetch_data()
  - `error_type` - Type of error to check for
- **Returns**: `True` if error found, `False` otherwise
- **Messages**: User-friendly error explanations

#### `main()`
- **Purpose**: Main application loop and CLI interface
- **Features**: Menu selection, repeated fetching, user interaction

## Learning Outcomes

This project teaches you about:

- **HTTP Requests**: Using `requests` library to make API calls
- **JSON Parsing**: Automatically parsing JSON responses with `.json()`
- **Error Handling**: Try-except blocks for robust error management
- **API Integration**: Working with real-world public APIs
- **Type Hints**: Using Python type annotations for clarity
- **CLI Design**: Building interactive command-line interfaces
- **Data Formatting**: Presenting data in user-friendly formats

## Example Output

```
⏳ Fetching data from Random Joke (JokeAPI)...

============================================================
API Response:
============================================================
Category: Programming

Setup: Why do programmers prefer dark mode?
Delivery: Because light attracts bugs!
============================================================
```

## Error Handling Examples

**Network Error:**
```
❌ Error: Failed to fetch data from API
   Possible causes:
   - Network connection issue
   - API server is down
   - Invalid URL
```

**API Error:**
```
❌ API Error: Invalid request parameters
```

## Customization

### Add a New API

Edit the `apis` dictionary in the `main()` function:

```python
apis = {
    "1": {
        "name": "Your API Name",
        "url": "https://api.example.com/endpoint",
        "type": "general"  # or custom format name
    },
    ...
}
```

### Custom Display Format

Add a new condition in `display_data()` for your API format:

```python
if api_type == "your_api":
    # Custom formatting logic
    print(data['custom_field'])
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'requests'` | Run `pip install requests` |
| `Connection timeout` | Check your internet connection and API URL |
| `Invalid JSON` | The endpoint may not return JSON. Check the API documentation |

## Tips

💡 **Use timeout**: The `requests.get()` call includes a 5-second timeout to prevent hanging  
💡 **Type hints**: Help identify bugs and make code more readable  
💡 **Error messages**: Provide helpful guidance for debugging  
💡 **Always validate**: Check if API response is valid before displaying

## License

Free to use and modify for learning purposes.

## Next Steps

🚀 **Advanced Ideas:**
- Add API response caching
- Export results to CSV/JSON files
- Add command-line arguments (--api-url, --format)
- Create a config file for saving favorite APIs
- Add authentication support (API keys)
- Implement rate limiting
