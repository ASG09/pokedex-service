import requests
from typing import Any, Optional


class PokeAPIClient:
    """
    A client for the PokeAPI.
    """
    base_url = "https://pokeapi.co/api/v2/"

    def get(self, endpoint: str) -> Optional[dict[str, Any]]:
        """Fetches data from PokeAPI."""
        url = f"{PokeAPIClient.base_url}{endpoint}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
