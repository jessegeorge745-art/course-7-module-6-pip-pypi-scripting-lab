"""
fetch_data.py
Fetches a post from a public API using requests and writes it to a .txt file.
"""

import requests
from datetime import datetime


def fetch_data(url: str) -> dict:
    """Fetch JSON data from the given URL. Returns empty dict on failure."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}


def save_to_file(data: dict, filename: str) -> None:
    """Write fetched data fields to a text file."""
    with open(filename, "w") as file:
        file.write(f"Post ID: {data.get('id', 'N/A')}\n")
        file.write(f"Title: {data.get('title', 'N/A')}\n")
        file.write(f"Body: {data.get('body', 'N/A')}\n")
        file.write(f"Fetched at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    post = fetch_data(url)

    if post:
        output_file = "fetched_post.txt"
        save_to_file(post, output_file)
        print(f"Fetched Post Title: {post.get('title', 'No title found')}")
        print(f"Output saved to {output_file}")
    else:
        print("Failed to fetch data.")