import requests
import json
from typing import Optional, Dict, Any


def fetch_data(api_url: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(api_url, timeout=5)
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def display_data(data: Dict[str, Any], api_type: str = "general") -> None:
    if not data:
        print("No data to display")
        return
    
    print("\n" + "=" * 60)
    print("API Response:")
    print("=" * 60)
    
    if api_type == "joke":
        # Format for JokeAPI
        if data.get("type") == "single":
            print(f"Category: {data.get('category', 'N/A')}")
            print(f"\n{data.get('joke', 'N/A')}")
        elif data.get("type") == "twopart":
            print(f"Category: {data.get('category', 'N/A')}")
            print(f"\nSetup: {data.get('setup', 'N/A')}")
            print(f"Delivery: {data.get('delivery', 'N/A')}")
    else:
        # Generic JSON display
        print(json.dumps(data, indent=2))
    
    print("=" * 60 + "\n")


def handle_errors(response_data: Optional[Dict[str, Any]], 
                  error_type: str = "api") -> bool:
    if response_data is None:
        print("❌ Error: Failed to fetch data from API")
        print("   Possible causes:")
        print("   - Network connection issue")
        print("   - API server is down")
        print("   - Invalid URL")
        return True
    
    if isinstance(response_data, dict) and response_data.get("error"):
        print(f"❌ API Error: {response_data.get('error')}")
        return True
    
    return False


def main() -> None:
    print("🔗 Welcome to API Data Fetcher!")
    print("=" * 60)
    print("This tool fetches data from public APIs and displays results.\n")
    
    # Example API endpoints
    apis = {
        "1": {
            "name": "Random Joke (JokeAPI)",
            "url": "https://v2.jokeapi.dev/joke/Any",
            "type": "joke"
        },
        "2": {
            "name": "Random User",
            "url": "https://randomuser.me/api/",
            "type": "general"
        },
        "3": {
            "name": "Cat Facts",
            "url": "https://catfact.ninja/random",
            "type": "general"
        },
        "4": {
            "name": "Custom URL",
            "url": None,
            "type": "general"
        }
    }
    
    while True:
        print("\nAvailable APIs:")
        for key, api in apis.items():
            if api['url']:
                print(f"  {key}. {api['name']}")
            else:
                print(f"  {key}. {api['name']}")
        print("  5. Exit")
        
        choice = input("\nSelect an API (1-5): ").strip()
        
        if choice == "5":
            print("👋 Thank you for using API Data Fetcher!")
            break
        
        if choice not in apis:
            print("❌ Invalid choice. Please select 1-5.")
            continue
        
        selected_api = apis[choice]
        api_url = selected_api["url"]
        
        # Handle custom URL
        if choice == "4":
            api_url = input("Enter the API URL: ").strip()
            if not api_url:
                print("❌ URL cannot be empty.")
                continue
        
        print(f"\n⏳ Fetching data from {selected_api['name']}...")
        
        # Fetch data
        data = fetch_data(api_url)
        
        # Handle errors
        if handle_errors(data, error_type="api"):
            continue
        
        # Display data
        display_data(data, api_type=selected_api["type"])
        
        # Ask if user wants to fetch again
        repeat = input("Fetch again? (y/n): ").strip().lower()
        if repeat != "y":
            print("\n👋 Thank you for using API Data Fetcher!")
            break


if __name__ == "__main__":
    main()
