import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FirefliesWrapper:
    def __init__(self):
        self.api_key = os.getenv("FIREFLIES_API_KEY")
        self.base_url = "https://api.fireflies.ai/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def fireflies_query(self, query):
        response = requests.post(
            self.base_url,
            json={"query": query},
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def get_users(self):
        query = """
        query {
            users {
                id
                name
                email
            }
        }
        """
        return self.fireflies_query(query)

# Remove the following lines:
# fireflies = FirefliesWrapper()
# users_data = fireflies.get_users()
