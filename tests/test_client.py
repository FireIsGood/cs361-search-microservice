# Code adapted from https://github.com/max-osu/ms_top_scores test_client.py
import requests
import json

# Localhost -> 127.0.0.1
# Port Number -> 5155
BASE_URL = "http://127.0.0.1:5155"


def pretty_print(title, response):
    """Print in style."""
    print(f"\n---- {title} ----")
    print(f"Status code: {response.status_code}")
    # Parse body, if there is a body, and print in formatted JSON string.
    try:
        data = response.json()
        print(json.dumps(data, indent=2))
    # Return error message.
    except ValueError:
        print(response.text)


# Dynamically generated database entry ID
db_entry_id: str = ""


def main():
    # 1. Test GET /all-values
    resp = requests.get(f"{BASE_URL}/all-values")
    pretty_print("1. GET /all-values (list all searchable values)", resp)

    # 2. Test POST /search
    resp = requests.post(f"{BASE_URL}/search", json={"query": "sun"})
    pretty_print("1. POST /search (Search for 'hi')", resp)

    # 3. Test POST /search
    resp = requests.post(
        f"{BASE_URL}/search", json={"query": "sun", "options": {"caseSensitive": False}}
    )
    pretty_print("1. POST /search (Search for 'hi')", resp)


if __name__ == "__main__":
    main()
