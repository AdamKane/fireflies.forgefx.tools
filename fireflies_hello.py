import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("FIREFLIES_API_KEY")

# Set up the API endpoint and headers
url = "https://api.fireflies.ai/graphql"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define a simple GraphQL query to get user information
query = """
query {
    users {
        id
        name
        email
    }
}
"""

# Make the API request
response = requests.post(url, json={"query": query}, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Hello, Fireflies API!")
    print("User information:")
    for user in data.get("data", {}).get("users", []):
        print(f"- {user['name']} ({user['email']})")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
