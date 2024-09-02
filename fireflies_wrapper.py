import os
import requests
import pytest
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

    def fireflies_query(self, query: str) -> dict:
        try:
            response = requests.post(
                self.base_url,
                json={"query": query},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return {}

    def get_users(self) -> dict:
        query = """
            query {
                users {
                    user_id
                    email
                    name
                    num_transcripts
                    recent_transcript
                    recent_meeting
                    minutes_consumed
                    is_admin
                }
            }
        """
        response = self.fireflies_query(query)
        data = response.get("data", {})
        users = data.get("users", [])
        return users
    
    def get_user_count(self) -> int:
        users = self.get_users()
        return len(users)

def test_get_users():
    fireflies = FirefliesWrapper()
    users_data = fireflies.get_users()

    user_count = len(users_data)
    assert user_count > 0, "No users found"


